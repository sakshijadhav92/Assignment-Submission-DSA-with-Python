# Function to demonstrate printing pattern of numbers
def pattern(n):
	
	# initialising starting number 
	num = 0
	# outer loop to handle number of rows
	for i in range(0, n):
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i):
				# printing number
			print(num,end=" ")
			# incrementing number at each column
		num = num + 1
		# ending line after each row
		print("\r")

# Driver code
n = 6
pattern(n)
   