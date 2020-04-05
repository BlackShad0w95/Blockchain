import functools
from hash_util import  hash_block
import json
from block import Block
from transaction import Transaction

from verification import Verification
MINING_REWARD = 10

# Initializing our empty blockchain list
blockchain = []
# Unhandled transactions
open_transaction = []
owner = 'Domi'
# Registered participants: Ourself + other people sending/ receiving coins
participants = {'Domi'}
# participants = set()


def load_data(): 
    # PICKLE
    # with open('blockchain.p', mode='rb') as f:
    #     file_content = pickle.loads(f.read())
    #     global blockchain
    #     global open_transaction
    #     blockchain = file_content['chain']
    #     open_transaction = file_content['ot']

    # JSON
    global blockchain
    global open_transaction
    try:
        with open('blockchain.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                updated_block = Block(block['index'],
                                      block['previous_hash'],
                                      converted_tx,
                                      block['proof'],
                                      block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transaction = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transaction:
                updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
                updated_transactions.append(updated_transaction)
            open_transaction = updated_transactions
    except (IOError, IndexError):
        genesis_block = Block(0, '', [], 100, 0)
        # Initializing our empty blockchain list
        blockchain = [genesis_block]
        # Unhandled transactions
        open_transaction = []
    finally:
        print("cleanup")


load_data()


def save_data():
    # JSON
    try:
        with open('blockchain.txt', mode='w') as f:
            saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash,
                                                                 [tx.__dict__ for tx in block_el.transactions],
                                                                 block_el.proof, block_el.timestamp)
                                                           for block_el in blockchain]]
    #dict without .copy() because we not manipulate block
            f.write(json.dumps(saveable_chain))
            f.write('\n')
            saveable_tx = [tx.__dict__ for tx in open_transaction]
            f.write(json.dumps(saveable_tx))
    except IOError:
        print("Saving failed")


    # PICKLE
    # with open('blockchain.p', mode='wb') as f:
    #     save_data = {
    #         'chain': blockchain,
    #         'ot': open_transaction
    #     }
    #     f.write(pickle.dumps(save_data))

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    verifier = Verification()
    while not verifier.valid_proof(open_transaction, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in blockchain]
    open_tx_sender = [tx.amount for tx in open_transaction if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount_sent = 0
    # calculate a total amount of coins sent
    # for tx in tx_sender:
    #    if len(tx) > 0:
    #        amount_sent += tx[0]
    # this fetches received coin amount of transaction that we already
    # We ignore open transaction here
    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]



# def add_transaction(transaction_amount, last_transaction=[1]):
#     if last_transaction == None:
#         last_transaction = [1]
#     blockchain.append([last_transaction, transaction_amount])


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
        :sender: The sender of the coins
        :recipient:
        :amount:
    """
    # transaction = {'sender': sender,
    #                'recipient': recipient,
    #                'amount': amount,
    #                }
    transaction = Transaction(sender, recipient, amount)
    verifier = Verification()
    if verifier.verify_transaction(transaction, get_balance):
        open_transaction.append(transaction)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print("Hash is:{}".format(hashed_block))
    proof = proof_of_work()
    print(proof)
    reward_transaction = Transaction('MINING', owner, MINING_REWARD)
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    copied_transactions = open_transaction[:]
    copied_transactions.append(reward_transaction)
    # hashed_block = ''
    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)

    # print(hashed_block)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    # save_data()
    return True




    # 2nd solution
    # is_valid = True
    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    # return is_valid

    # 1st solution
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    # return is_valid



