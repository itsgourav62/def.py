import sys 
sum=0
while True:
    x=int(input('Enter the number(999 ends):'))
    if x== 999:
        sys.exit(0)
    sum+=x
    print('Sum is',sum)

x1=eval(input('Entry x1?'))#(eval)user input
print('x1=',x1, 'type:',type(x1))