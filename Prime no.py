n=int(input("Enter a number: "))
flag=1
for i in range(2,n//2+1):
    if(n%i==0):
        flag=0
        break
if(flag==1):
  print("True")
else:
    print("False")