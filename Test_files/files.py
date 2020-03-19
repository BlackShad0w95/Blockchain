""" Write content to the file"""
# f = open('demo.txt', mode='w')
# f.write('Hello from python!')
# f.close()
#
# user_input = input('Provide data:')
"""Read content from the file"""
# f = open('demo.txt', mode='r')
# file_content = f.read()
# print(file_content)
# f.close()

"""Append content to the file"""
# f = open('demo.txt', mode='r')
# f.write('Added new comething to the file\n')
# file_contnt = f.readlines()
# print(file_contnt)
# f.close()
#
# for line in file_contnt:
#     print(line[:-1])

# line = f.readline()
# print(line)
# print(all(line))

# while line:
#     print(all(line))
#     print(line)
#     line = f.readline()

"""With statement - automatically closed file by Python"""
with open('demo.txt', mode = 'r') as f:
    line = f.readlines()
    print(line[0][2])

print('Done')
