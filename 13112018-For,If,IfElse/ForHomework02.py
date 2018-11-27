import math
z ='' 
for j in range(10,0,-1):
    for i in range(j-5):
        z += ' * '  
    if j<=4:
        for u in range(6-j):
            z += ' * ' 
    if j!=5:
        z+= '\n'        
    




print(z)