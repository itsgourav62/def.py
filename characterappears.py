#Write a program to count the number of times a character appears in a given string
str = input("Enter a string : ")
char = input("Enter the character : ")
i = 0
t = 0

while(i < len(str)):
    if(str[i] == char):
        t= t + 1
    i = i + 1

print("Total number of times it appeared = " , t)