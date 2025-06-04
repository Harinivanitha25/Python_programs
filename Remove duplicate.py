l=[int(x) for x in input("Enter a list: ").split()]
for i in range(0,len(l)-2):
     if(l[i]==l[i+1]):
            l.pop(i)
print("After removing duplicate: ",l)