def ChangeMe( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4] # This would assign a new reference in mylist
    print("Values inside the Change Me function:  {}".format(mylist))
    return

def AddToMe( mylist ):
    "This appends a passed list into this function"
    mylist.append(0)
    mylist.append(1)
    mylist.append(2)
    print("Values inside the AddTo Me function:  {}".format(mylist))
    return

# Now you can call changeme function
mylist = [10,20,30]
print("Values:  {}".format(mylist))

ChangeMe( mylist )
print("Values outside th function:  {}".format(mylist))

AddToMe( mylist )
print("Values outside the function:  {}".format(mylist))

ChangeMe( mylist )
print("Values outside the function:  {}".format(mylist))