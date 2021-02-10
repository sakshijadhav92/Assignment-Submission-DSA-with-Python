import numpy as np
my_list = [2,4,6,8,10,18,20]
my_array = np.array(my_list)
# printing my_array
print("Before Deletion My Array :",my_array)
# printing the type of my_array
print(type(my_array))
#delete from any position 
num = int(input("Enter Position from where u want to delete:"))
my_array = np.delete(my_array, num-1)
# printing the my_array
print("After Deletion My Array :",my_array)