n=int(input("Enter a number: "))
n1,n2=0,1
a=n
l=[0,1]
for i in range(2,n):
    a=n1+n2
    l.append(a)
    n1=n2
    n2=a
print(l)
    
