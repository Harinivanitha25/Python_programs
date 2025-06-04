n=int(input("Enter a number: "))
n1,n2=0,1
a=n
print("0\n1")
for i in range(2,n):
    a=n1+n2
    print(a)
    n1=n2
    n2=a
    
