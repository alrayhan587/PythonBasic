# Format() takes the passed arguments

salary = 100000
txt = "Hello, My name is Al Rayhan. As you know my salary is {}tk"
print(txt.format(salary))


# We can format multiple arguments.
# At the time of passing arguments we have to "follow the order"
age = 25
txt = "Hello My name is Al Rayhan. My age is {} years. as you already know my salary is {}tk"
print(txt.format(age, salary))

# If you don't wanna follow the order
# You have to use index numbers like {2}
id = 567
txt = "Hello. Its Al Rayhan. ID {1}. my age is {2} and my salary is {0}tk"
print(txt.format(salary, id, age))
