# print("Hello,World")
a = "Hello,World"
print(a)

print(a[2:5])  # This line print the string from index2 to index5
print(a[3:9])  # Different value

print(a[2:15])  # If taken value is longer than length
# It doesn't show any problem. Simply printed to it's assigned limit


# 1. Slicing string from selected value
print("Selected part", a[2:6])

# 2. Slicing string from any index to end
print("Any index to end", a[2:])

# 3. Slicing string from start to any index
print("Start to any index", a[:6])

# 4. Slicing string using negative value
print("Using Negative Index", a[-5:-2])
# At the case of negative index count start from rear of the string
