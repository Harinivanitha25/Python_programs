n=int(input("Enter a number to palindrome or not: "))
sum=0
a=n
while(n>0):
  rem=n%10
  sum=sum*10+rem
  n=n//10
if(a==sum):
 print("Palindrome")
else:
 print("Not a Palindrome")