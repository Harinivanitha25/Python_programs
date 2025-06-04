l= [int(x) for x in input("Enter a list: ").split()]
l1=[]
for i in range(1,len(l)+1):
    l1.append(l[-i])
print(l1)
  