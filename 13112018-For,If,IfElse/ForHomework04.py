def UD_triangle(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(n, 0,-1): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k += 1
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 


def simplerUD_Triangle(n):
	z=''
	for num in range(n):
		for num1 in range(num):
			z+="   "
		for num2 in range((n*2)-(num*2)-1):
			z+=" * "
		z+= "\n"

	print(z)

# Driver Code 
n = int(input('Input Size: '))
# UD_triangle(n) 
simplerUD_Triangle(n)
