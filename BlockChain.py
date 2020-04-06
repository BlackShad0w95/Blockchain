import functools
from hash_util import  hash_block
import json
from block import Block
from transaction import Transaction

from verification import Verification
MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        # Initializing our empty blockchain list
        genesis_block = Block(0, '', [], 100, 0)
        self.chain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id


    @property
    def chain(self):
        return self.__chain[:]

    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        # PICKLE
        # with open('blockchain.p', mode='rb') as f:
        #     file_content = pickle.loads(f.read())
        #     global blockchain
        #     global open_transaction
        #     blockchain = file_content['chain']
        #     open_transaction = file_content['ot']

        # JSON
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
                self.chain = updated_blockchain
                open_transaction = json.loads(file_content[1])
                updated_transactions = []
                for tx in open_transaction:
                    updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
        except (IOError, IndexError):
            print("Handled exceptions")
        finally:
            print("cleanup")

    def save_data(self):
        # JSON
        try:
            with open('blockchain.txt', mode='w') as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash,
                                                                     [tx.__dict__ for tx in block_el.transactions],
                                                                     block_el.proof, block_el.timestamp)
                                                               for block_el in self.__chain]]
        #dict without .copy() because we not manipulate block
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
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

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    def get_balance(self):
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant]
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
        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.__chain]
        amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        # amount_received = 0
        # for tx in tx_recipient:
        #     if len(tx) > 0:
        #         amount_received += tx[0]
        return amount_received - amount_sent


    def get_last_blockchain_value(self):
        """Return the last value of the current blockchain"""
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]


    def add_transaction(self, recipient, sender, amount=1.0):
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
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False


    def mine_block(self):
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        print("Hash is:{}".format(hashed_block))
        proof = self.proof_of_work()
        print(proof)
        reward_transaction = Transaction('MINING', self.hosting_node, MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__chain), hashed_block, copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
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



