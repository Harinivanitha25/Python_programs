l=[int(x) for x in input("Enter a list: ").split()]
newl=l
for i in range(0,len(l)):
    for j in range(i+1,len(l)-1):
        if(l[i]==l[j]):
            newl.pop(j)
print("After removing duplicate: ",newl)
