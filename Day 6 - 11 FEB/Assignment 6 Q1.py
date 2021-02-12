
def enqueue():
    global size, f, r
    data=int(input("Enter data :"))
    if r == size - 1:
        print('Queue Overflow')
        return
    if r == -1:
        f = r = 0
    else:
        r += 1
    q.append(data)
    return

def dequeue():
    global size, f, r
    if r == -1:
        print('Queue Underflow')
        return
    else:
        r-=1
        e=q.pop(0)
        print("Element Removed!!:",e)
        return
    
def display():
    global size, f, r
    if f == -1:
        print('No item to display')
        return
    for i in range(f, r + 1):
        print(q[i], end = " ")
    return

q = []
f,r = -1,-1
size=int(input("Enter the size of Queue:"))
while True:
    print("\nSelect the Operation:1.Add 2.Delete 3. Display 4. Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Option!!!")





 
   