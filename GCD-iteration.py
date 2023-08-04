#Python program to calculate GCD using iteration
a = float(input("Enter the First Value: "))
b = float(input("Enter the Second Value: "))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i = i + 1
    
print("\n GCD of {0} and {1} = {2}".format(a, b, gcd))