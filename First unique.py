a=list(input("Enter a word: "))
flag=0
for i in range(0,len(a)):
    flag=0
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
         flag=1
    if(flag==0):
       b=a[i]
       break
print("The unique first letter -",b)
        
    