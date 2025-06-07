l= [int(x) for x in input("Enter a list: ").split()]
flag=0
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            print("The Duplicate: ",l[i])
            flag=1
if(flag==0):
     print("No duplicate")