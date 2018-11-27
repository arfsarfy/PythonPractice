def triangle(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(0, n): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k = k - 1
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 

def UD_triangle(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(n, -1,-1): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k-n): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k += 1
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 

def simplerTriangle(n):
	z=''
	for num in range(n):
		for num1 in range(0,n-1-num):
			z+="   "
		for num2 in range(0,(num*2)+1):
			z+=" * "
		if num == n-1:
			break
		z+= "\n"
	
	print(z)

def simplerUD_Triangle(n):
	z=''
	for num in range(1,n):
		for num1 in range(num):
			z+="   "
		for num2 in range((n*2)-(num*2)-1):
			z+=" * "
		z+= "\n"

	print(z)



# Driver Code 
n = int(input('Input Size: '))
# triangle(n)
# UD_triangle(n)

simplerTriangle(n)
simplerUD_Triangle(n)
