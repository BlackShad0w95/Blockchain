class Node:

    def __init__(self):
        self.blockchain = []

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
                self.print_blockchain_elements()
            elif user_choice == '4':
                print(participants)
            elif user_choice == '5':
                verifier = Verification()
                if verifier.verify_transactions(open_transaction, get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print("Input was not valid")
            verifier = Verification()
            if not verifier.verify_chain(blockchain):
                self.print_blockchain_elements()
                print('Invalid blockchain')
                break
            # print("My (Domi) balance: {}".format(get_balance('Domi')))
            print('Balance of {} is {:6.2f}'.format('Domi', get_balance('Domi')))
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
        if len(self.blockchain) < 1:
            print("No value at all")
        for block in self.blockchain:
            print('Output of the block')
            print(block)
        else:
            print('--' * 20)