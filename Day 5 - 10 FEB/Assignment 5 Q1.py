def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1 -i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("Bubble Sort :",arr)

arr = [int(i) for i in input('Enter values: ').split()]
bubble_sort(arr)
   