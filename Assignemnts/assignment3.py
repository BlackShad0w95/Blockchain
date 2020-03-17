# Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
person1 = {'name': 'Ola',
           'age': 4,
           'hobbies': ['karate', 'judo', 'painting']
           }

person2 = {'name': 'Kasia',
           'age': 24,
           'hobbies': ['testing']
           }

person_list = [person1, person2]
for person in person_list:
    print(person["name"])

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

names_list = [person["name"] for person in person_list]
print(names_list)

# 3) Use a list comprehension to check whether all persons are older than 20.

older_20 = all([person["age"] > 20 for person in person_list])
print(older_20)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
new_names_list = names_list[:]
new_names_list = [names_list.copy() for person in names_list]
print(new_names_list)
new_names_list[1] = 'o'
print(new_names_list)
print(names_list)
copied_person = [person.copy() for person in person_list]

# 5) Unpack the persons of the original list into different variables and output these variables.

# a, b = [person for person in person_list]
a, b = person_list
print(a)
print(b)
