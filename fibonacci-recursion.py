#Python program to find the fibonacci series using recursion
def recursion_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recursion_fibo(n-1) + recursion_fibo(n-2)) 
nterms=int(input('Enter the number:'))
if nterms <= 0:  
   print("Invalid Option!!")  
else:  
   print("Fibonacci Series:")  
   for i in range(nterms):  
       print(recursion_fibo(i))  