n=int(input("Enter No. Elements in List:"))
list1=[]
even=[]
for i in range(0,n):
    s=int(input("Enter Element in List : "))
    list1.append(s)

for i in range(0,n):
    a=list1
    if(a[i] % 2 == 0):
        even.append(a[i])


print("Even Numbers in List: ",even)
