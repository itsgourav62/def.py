# Python 3 program to find factorial of given number using recursion
def factorial(n):
	
	
	return 1 if (n==1 or n==0) else n * factorial(n - 1);


num = int(input('Enter the number to find its factorial: '))
print("Factorial of",num,"is",
factorial(num))


