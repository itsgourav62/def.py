def factorial(number):
    '''This function calculates the factorial of a number'''
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
        return -1
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def factorial_without_recursion(number):
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
        return -1
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    return fact

if __name__ == '__main__':
    userInput = int(input('Enter the number to find its factorial: '))
    print('Factorial using Recursion of', userInput, 'is:', factorial(userInput))
    print('Factorial without Recursion of', userInput, 'is:', factorial_without_recursion(userInput))