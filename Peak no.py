a=[(x) for x in input("Enter a list: ").split()]
for i in range(1,len(a)-1):
    if(a[i-1]<a[i]>a[i+1]):
       print(a[i])
