# x = [40,100,1,5,25,10]

# # sorted_x = sorted(x)
# # print('the unsorted data:',x)
# # print('sorted',sorted_x)
# # print(sorted_x[(len(sorted_x))-1])

#selection sort /bubble sort

def Bubblesort(x=list):
    n= len(x)
    for i in range(n):
        print('i:',i)
        for j in range(n-i-1) :
            if x[j]<x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
            print(x)            
    # print(x)

def Selectionsort(x=list):
    n=len(x)
    for i in range(n):
        idx=i
        for j in range(i+1,n):
            if x[j]<x[idx]:
                idx = j
        x[i],x[idx]=x[idx],x[i]
    print(x)

x=[3,2,4,5,2,3]
Bubblesort(x)
# Selectionsort(x)