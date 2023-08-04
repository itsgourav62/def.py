#Python program to find the fibonacci series using iteration
first,second=0,1
n = int(input("Enter a number  : "))
print("Fibonacci series : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
    print(result)