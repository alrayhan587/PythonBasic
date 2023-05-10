# count(value,start,end) method used to count the given variable
txt = "Hello my name is al rayhan. I live in dhaka. My hometown is barisal"
x = txt.count("m")
print(x)
print(txt.count("m", 8, 30))


# find(" ") method used to find particular value from any string
print(txt.find("m"))
# index(" ") method works as same as find()
print(txt.index("m"))
#  *** find() and index() method working process is same. Main difference between them is their return value at invalid parameter ***
#  If the value is not found
# index() raises an exceptional error
# where on the other side find() returns -1


# join() methods take all the item iterable. and joins them in one string
mytuple = ("john")
print("#".join(mytuple))

mytuple = ("john", "Vicky", "Rayhan")
print("#".join(mytuple))


# partition divide string into 3 parts
# ['Everything before match','matching part','Everything after match']
txt = "I would love to eat a lot of banana"
print(txt.partition("to eat"))
