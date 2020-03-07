# 1) Create a list of names and use a for loop to output the length of each name (len() ).
# 2) Add an if  check inside the loop to only output names longer than 5 characters.
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
# 4) Use a while  loop to empty the list of names (via pop() )

name_list = []


def get_name():
    for i in range(3):
        name = input()
        name_list.append(name)
    return name_list


def get_name_length(list_of_names):
    for name in list_of_names:
        if len(name) > 5:
            if 'n' in name or 'N' in name:
                print(name)


def empty_list(list_of_name):
    while len(list_of_names) is not 0:
        print(list_of_names.pop())


list_of_names = get_name()
get_name_length(list_of_names)
print('-'*30)
empty_list(list_of_names)
print('-'*30)
print(list_of_names)

