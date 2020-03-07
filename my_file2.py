number_list = [1, 2, 3, -5]

print(all([el > 0 for el in number_list]))
print(any([el > 0 for el in number_list]))