# x = [40,100,1,5,25,10]

# sorted_x = sorted(x)
# print('the unsorted data:',x)
# print('sorted',sorted_x)
# higest = sorted_x[(len(sorted_x))-1]
# lowest = sorted_x[0]
# print('Higest number from the list is {} and the lowest is {}'.format(higest,lowest))

def MaxMin(x=list):
    n = len(x)
    idx_max, idx_min = 0, 0
    for j in range(n):
        if x[j]>x[idx_max]:
            idx_max=j
        if x[j]<x[idx_min]:
            idx_min=j
    print('max in array :',x[idx_max])
    print('min in array :',x[idx_min])

x=[0,4,33,12,15,0]
MaxMin(x)
            


            
