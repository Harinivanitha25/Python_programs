n=int(input("Enter a number: "))
v=[]
val=0
while(n>0):
  a=n%2
  v.append(a)
  n=n//2
print("The no of 1 in bit representation",v.count(1))
  