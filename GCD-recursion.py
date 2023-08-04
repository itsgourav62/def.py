# Python Program to find GCD of Two Numbers using recursion

def findgcd(a, b):
    if(b == 0):
        return a;
    else:
        return findgcd(b, a % b)
    
num1 = float(input("Enter the First Value: "))
num2 = float(input("Enter the Second Value: "))

gcd = findgcd(num1, num2)
print("\n GCD of {0} and {1} = {2}".format(num1, num2, gcd))