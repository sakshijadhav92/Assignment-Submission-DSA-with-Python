def selection_sort(arr):
    for i in range(len(arr)):
        min_value=i
        for j in range(i+1,len(arr)):
            if(arr[min_value] > arr[j]):
                min_value=j
                arr[i],arr[min_value]=arr[min_value],arr[i]
    print("Selection Sort :",arr)

arr = [int(i) for i in input('Enter values: ').split()]
selection_sort(arr)
   