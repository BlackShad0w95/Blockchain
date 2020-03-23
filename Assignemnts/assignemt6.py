# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# # 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# # 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# # 4) Adjust the logic to load the file content to work with pickled/ json data.

import json
statement = True
data_to_saved = []

while statement is True:
    print("1: Press 1 to add new value")
    print("2: Press 2 to show saved value")
    print("3: Press q to add new value")
    choice = input()
    if choice == '1':
        print("Provide some input to be saved")
        data_tobe_saved = input()
        data_to_saved.append(data_tobe_saved)
        print("Data will be saved")
        with open("data_tosaved.txt", mode='w') as f:
            f.write(json.dumps(data_to_saved))
    if choice == '2':
        print("Below you can find sata stored in saved .txt file")
        with open("data_tosaved.txt", mode='r') as f:
            file_content = json.loads(f.read())
            print(file_content)
    if choice == 'q':
        statement = False
    print("Out of if loop")

print("Out of while loop")
