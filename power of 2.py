n=int(input("Enter a number: "))
f=0
while(n>2):
  if(n%2==0):
    n=n/2
  else:
     f=1
     break
if(f==1):
 print("Not a Power of 2")
else:
 print("Power of 2")