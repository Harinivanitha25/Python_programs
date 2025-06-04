l = [int(x) for x in input("Enter List: ").split()]
t = int(input("Enter the Target: "))
flag=1
for i in range(0,(len(l)-1)): 
    for j in range(i+1,len(l)):
        if((l[i]+l[j])==t):
            print("Numbers are",l[i],l[j])
            flag=0
if(flag==1):
    print("No 2 sum found")