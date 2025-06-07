a=[(x) for x in input("Enter a list 1: ").split()]
b=[(x) for x in input("Enter a list 2: ").split()]
for i in b:
    a.append(i)
a.sort()
print(a)