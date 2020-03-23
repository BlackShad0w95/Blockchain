import functools
from collections import OrderedDict
from hash_util import hash_string_256, hash_block
import json
import pickle

MINING_REWARD = 10

genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transactions': [],
                 'proof': 100
                 }
# Initializing our empty blockchain list
blockchain = [genesis_block]
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
    with open('blockchain.txt', mode='r') as f:
        file_content = f.readlines()
        global blockchain
        global open_transaction
        blockchain = json.loads(file_content[0][:-1])
        updated_blockchain = []
        for block in blockchain:
            updated_block = {
                'previous_hash': block['previous_hash'],
                'index': block['index'],
                'proof': block['proof'],
                'transactions': [OrderedDict([('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
            }
            updated_blockchain.append(updated_block)
        blockchain = updated_blockchain
        open_transaction = json.loads(file_content[1])
        updated_transactions = []
        for tx in open_transaction:
            updated_transaction = OrderedDict([('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
            updated_transactions.append(updated_transaction)
        open_transaction = updated_transactions


load_data()


def save_data():
    # JSON
    with open('blockchain.txt', mode='w') as f:
        f.write(json.dumps(blockchain))
        f.write('\n')
        f.write(json.dumps(open_transaction))

    # PICKLE
    # with open('blockchain.p', mode='wb') as f:
    #     save_data = {
    #         'chain': blockchain,
    #         'ot': open_transaction
    #     }
    #     f.write(pickle.dumps(save_data))


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transaction, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transaction if tx['sender'] == participant]
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
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
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


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    if sender_balance >= transaction['amount']:
        return True
    return False


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
    transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transaction.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print("Hash is:{}".format(hashed_block))
    proof = proof_of_work()
    print(proof)
    reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
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
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': copied_transactions,
             'proof': proof
             }
    blockchain.append(block)
    # save_data()
    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please:\n '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice:\n')
    return user_input


def print_blockchain_elements():
    if len(blockchain) < 1:
        print("No value at all")
    for block in blockchain:
        print('Output of the block')
        print(block)
    else:
        print('--' * 20)


def verify_chain():
    """Verify the current blockchain."""
    # 3rd solution
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print("Proof of work is invalid")
            return False
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


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transaction])
    # is_valid = True
    # for tx in open_transaction:
    #     if verify_transactions(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid



waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output recipients and participant')
    print('5: Transaction validity')
    print('h: Manipulate the chain')
    print('q: To quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed')
        print("Open trasaction: {}".format(open_transaction))
    elif user_choice == '2':
        if mine_block():
            open_transaction = []
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Domi', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("Input was not valid")
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain')
        break
    # print("My (Domi) balance: {}".format(get_balance('Domi')))
    print('Balance of {} is {:6.2f}'.format('Domi', get_balance('Domi')))
    print('Choice registered!')
else:
    print('User left!')

print('Done!')

