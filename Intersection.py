l1=[int(x) for x in input("Enter first list: ").split()]
l2=[int(x) for x in input("Enter second list: ").split()]
a=[]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if(l1[i]==l2[j]):
            a.append(l1[i])
            l2.pop(j)
            break;
print(a)
