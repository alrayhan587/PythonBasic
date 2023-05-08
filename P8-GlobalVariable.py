x = "hello world"


def myfunc1():
    print(x)


def myfunc2():
    x = "Fantastic"
    print(x)

# "Global" keyword also used for create global variable


def myfunc3():
    global x
    x = "I Love You"
    print(x)


myfunc1()
myfunc2()
print(x)
myfunc3()
print(x)

# Declaration of the function doesn't matter
# If we declare the function for once
# Then the global function will work for every call
# Like myfunc3 declare the global variable
# And it worked before it delcared
