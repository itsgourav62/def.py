#Count the occurrence of a specific object in a list
names=['Qiqi','Ren','Yaga','Amber','Amber','Ren','Qiqi','Childe','Yaga']
d={}
for i in range(len(names)-1):
    x=names[i]
    c=0
    for j in range(i,len(names)):
        c=names.count(x)
    count=dict({x:c})
    if x not in d.keys():
        d.update(count)
print (d)