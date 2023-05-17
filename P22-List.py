# Q1. What is list
# Q2. How many way we can collect multiple data in python


# Lists are used to store multiple data in single variables.

mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0])
print(mylist[2])

# Characteristics of List
# 1.Ordered, 2.Changeable, 3.allow duplicate values

# The order of the list can't be changed. New items are only add on the end of the list.
print("Order of the list:", mylist)

# As List allow duplicates
yourlist = ["Rayhan", "Kabir", "Pakhi", "Nabodut", "Kabir", "Pakhi"]
print(yourlist)

# len() Function to determine how many items a list has
print("mylist has", len(mylist), "items")
print("yourlist has", len(yourlist), "items")


# A list can contain any data types
# The data types can be different each times
list1 = ["apple", 32, 65.6, True, False]
print("Different data type list:", list1)

# List are defined as an object and the data type of that object is 'list'

# List corstrutor can be used to create list
list2 = list(("ABC", "DEF", 90))  # Note: Double brackets required
print(list2)


# yourlist = ["Rayhan", "Kabir", "Pakhi", "Nabodut", "Kabir", "Pakhi"]
# Access to the list
print(yourlist[1])
print(yourlist[-1])
print(yourlist[2:5])  # Index 5 will not be collected
print(yourlist[2:])
print(yourlist[:4])  # Index $ is not taken
print(yourlist[-4:-1])


# yourlist = ["Rayhan", "Kabir", "Pakhi", "Nabodut", "Kabir", "Pakhi"]
# Mutate the value of the list

# 1. Change item value
yourlist[1] = "Hello"
print(yourlist)


# 2. Insert value using range ,
yourlist[1:3] = ["Hello"]
print(yourlist)

yourlist[1:4] = ["Eh", 6, 7, "tata", "Mair"]
print(yourlist)

# 3.Insert value by using insert command insert(index,item value)
yourlist.insert(2, "berry")
print(yourlist)


# yourlist = ["Rayhan", "Kabir", "Pakhi", "Nabodut", "Kabir", "Pakhi"]
# To add an item at the end of the list
yourlist.append("pakhi")
print(yourlist)

# yourlist.append("tho", "kobi") ERROR list.append() takes exactly one argument


# mylist = ["apple", "banana", "cherry"]
# yourlist = ["Rayhan", "Kabir", "Pakhi", "Nabodut", "Kabir", "Pakhi"]
mylist.extend(yourlist)
print("Extend List", mylist)


# REMOVE list item.
mylist.remove("Eh")
print(mylist)

# POP Function remove specific item
mylist.pop(2)
print("After deletion of index 2", mylist)

mylist.pop()  # Remove last item of the list
print("After deletion of last item of list", mylist)

# Remove specific item of the list
del mylist[3]
print(mylist)

del yourlist
# print(yourlist) This will cause error. successfully deleted yourlist

# If we don't wanna erase the whole list. just clear the list
print("Before clear", list2)
list2.clear()
print("After clear", list2)
