def multiflication(a, b):
    return a * b

breakpoint()

x = input("Enter first number: ")
y = input("Enter second number: ")

mul = multiflication(x,y)
print(mul)
# This code will not work as expected because input() returns a string, and we need to convert it to an integer or float before multiplying.