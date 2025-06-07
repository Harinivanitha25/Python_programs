n=int(input("Enter a three_digit number:"))
a=n
sum=0
r=0
while(n>0):
    r=n%10
    sum=sum+(r**3)
    n=n//10
if(sum==a):
  print("Given no is armstrong no")
else:
  print("Given no is not armstrong no")