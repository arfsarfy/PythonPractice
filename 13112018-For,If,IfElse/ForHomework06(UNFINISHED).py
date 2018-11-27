# n = int(input('Input Size: '))
n= 3
z=''
#ReversedDiamond
#3forloop - 1 left '*';1" ";1 right'*'
for num in range(n):
	for num1 in range(0,(n*2-1)):
		z+=" * "


        
            
	z+= "\n"
for num in range(1,n):
	for num1 in range(num):
		z+=" * "
	for num2 in range((n*2)-(num*2)-1):
		z+="   "
	z+= "\n"


print(z)





