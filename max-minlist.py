NumList = []
Number = int(input("Enter element length in list "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    NumList.append(value)
 
print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))
