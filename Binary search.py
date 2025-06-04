l=[int(x) for x in input("Enter list: ").split()]
k=int(input("Enter key: "))
beg=0
end=len(l)-1
def bin(l,k,beg,end):
    mid=(beg+end)//2
    if(l[mid]==k):
        print("Key found at",mid+1)
    elif(l[mid]>k):
        bin(l,k,beg,mid-1)
    else:
        bin(l,k,mid+1,end)
bin(l,k,beg,end)