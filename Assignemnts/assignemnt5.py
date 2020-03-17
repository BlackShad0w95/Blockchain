import random
import datetime

# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
ran_number = random.randint(0, 10)
print(ran_number)

ran_range = random.random()
print(ran_range)

# 2) Use the datetime library together with the random number to generate a random, unique value.
print(datetime.datetime.now())
ru = str(ran_number) + str(datetime.datetime.now())
print(ru)
