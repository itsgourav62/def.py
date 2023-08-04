from time import clock
sum=0
start=clock()
for n in range(1,100000001):
    sum+=n
elapsed=clock()-start
print("sum:",sum,"time:",elapsed)