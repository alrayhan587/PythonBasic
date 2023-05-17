# Identity operator works for objects

print("\nResult of <is> operator")
# "is" return "TRUE" if both variable are from same object
x = ["Rayhan", "Kabir"]
y = ["Rayhan", "Kabir"]
z = x

print(x is z)
# TRUE cause they are same object

print(x is y)
# FALSE cause they are not same object. They have same content but they are different object

print(x == y)
# TRUE {Difference between "==" and "is"}
# == check the content

print("\nChecking <is not> operator now:")
# "is not" return "FALSE" if both variable are not from same object
print(x is not z)
print(x is not y)


print("\nChecking Membership operator:")
# membership operator
# in and not in

a = ["apple", "banana"]
print("apple" in a)  # TRUE

print("banan" not in a)  # TRUE cause i mistook with spelling
