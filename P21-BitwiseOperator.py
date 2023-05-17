# There are several of bitwise operator
# AND(&) OR(|) NOT(~) XOR(^) ZERO_FILL_LEFT_SHIFT(<<) SIGNED_RIGHT_SHIFT(>>)

# As Bitwise operator basically divide them into bits and then do the operation

a = 6
b = 4

print("And operator:")
print(a & b)
# 6 = 0000 0000 0000 0110
# 4 = 0000 0000 0000 0100
# And opereation
# 4 = 0000 0000 0000 0100

# NOT Operation , all 16 bits will be inverts with opposite bit
print("\nNOT Operation of 3 is:")
print(~3)

# 3  = 0000 0000 0000 0011
# After NOT Operation
# -4 = 1111 1111 1111 1100


a = 3
print(f"\nLeft shift of {a} <2 times>:")
print(a << 2)
# 2 bits left shift
# 3=  0000 0000 0000 0011
# 12= 0000 0000 0000 1100

a = 1
print(f"\nRight shift of {a} <2 times>:")
print(a << 2)
# 2 times right shift
# 3=  0000 0000 0000 0001
# 4=  0000 0000 0000 0100
