# Python Program to find Sum of all Elements in a List

numList = []
total = 0

Number = int(input("Enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    numList.append(value)

for j in range(Number):
    total = total + numList[j]

print("\n The Sum of All Element in this List is : ", total)