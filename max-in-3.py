#Python program to find the max between 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

mx = a if a > b and a>c else b if b>c else c

print(mx)