userin=input('Input Numbers :')
arr = list(userin.split(' '))
print(arr)
z=''
row2={0:'| |',1:"  |",2:" _|",3:" _|",4:"|_|",5:"|_ ",6:"|_ ",7:"  |",8:"|_|",9:"|_|"}
row3={0:'|_|',1:"  |",2:"|_ ",3:" _|",4:"  |",5:" _|",6:"|_|",7:"  |",8:"|_|",9:" _|"}
for i in range(3):
    for n,num in enumerate(arr):
        if num == '':
            break

        num = int(num)
        if i == 0:
            if num == 1 or num == 4:
                z +="   "
            else:
                z +=" _ "
        elif i == 1:
            z += row2[num] 
        elif i == 2:
            z += row3[num]


    z+="\n"

print(z)

