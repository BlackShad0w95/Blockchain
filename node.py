from BlockChain import Blockchain
from uuid import uuid4
from verification import Verification


class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.id = "DOMI"
        self.blockchain = Blockchain(self.id)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Output recipients and participant')
            print('5: Transaction validity')
            print('q: To quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed')
                print("Open trasaction: {}".format(self.blockchain.get_open_transactions()))
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '5':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print("Input was not valid")
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain')
                break
            # print("My (Domi) balance: {}".format(get_balance('Domi')))
            print('Balance of {} is {:6.2f}'.format(self.id, self.blockchain.get_balance()))
            print('Choice registered!')
        else:
            print('User left!')

        print('Done!!')

    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction:')
        tx_amount = float(input('Your transaction amount please:\n '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        user_input = input('Your choice:\n')
        return user_input

    def print_blockchain_elements(self):
        if len(self.blockchain.chain) < 1:
            print("No value at all")
        for block in self.blockchain.chain:
            print('Output of the block')
            print(block)
        else:
            print('--' * 20)


node = Node()
node.listen_for_input()