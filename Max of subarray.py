l= [int(x) for x in input("Enter the list: ").split()]
t=int(input("Enter the target: "))
a=[]
for i in range(0,len(l)-1):
    s=l[i]
    a.append(s)
    for j in range(i,len(l)-1):
     s=s+l[j+1]
     a.append(l[j+1])
     if(s==t):
        print(a)
    a.clear()
    



