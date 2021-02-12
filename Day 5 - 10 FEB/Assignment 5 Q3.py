def insertion_sort(arr):
    for i in range(len(arr)):
        position=i
        current_value=arr[i]
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position-1]
            position = position-1
            arr[position] = current_value
    print("Insertion Sort :",arr)
    
arr = [int(i) for i in input('Enter values: ').split()]
insertion_sort(arr)  
   