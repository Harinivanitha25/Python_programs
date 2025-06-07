def swap(a,b):
    temp=l[a]
    l[a]=l[b]
    l[b]=temp
l=[int(x) for x in input("Enter list: ").split()]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
          swap(i,j)
print(l)

    