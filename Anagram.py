a=input("Enter a string 1: ")
b=input("Enter a string 2: ")
f=list(b)
l=[]
for i in b:
    for j in a:
        if(i==j):
           l.append(i)
           break
if(f==l):
    print("Anagram")
else:
    print("No Anagram")
        


