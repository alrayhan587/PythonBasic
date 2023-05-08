# Strings are array.

a = "Hello"
print(a[0])
print(a[2])
print(a[1])


for x in "banana":
    print(x)

# Loop also can be used after declaring string in variable
for x in a:
    print(x)

# Length of the string. To find the length of the string
# Code must be len("str")

print(len("Pappu"))
print(len(a))
print(len("Hello World"))  # Empty space between Hello world also counted

# Now I'm checking the string. Is the searching value is inside or not?

p = "Hello my name is al Rayhan"
print("al" in p)
print("al " in p)
print("al  " in p)  # There is only one empty space

# "not in" also works like "in"
print("al" not in p)
print("al   Ray" not in p)
