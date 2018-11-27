import math
arr = [2,4,5,5,1,4,3]
print(arr)
def meanf(arr):
    tot=0
    for item in arr:
        tot+=item
    avg = tot/len(arr)
    return avg
        
print(meanf(arr))

def median_(arr):
    n = len(arr)
    arr.sort()
    # for i in range(n):
    #     for j in range(n-1-i):
    #         if arr[j]>arr[j+1]:
    #             arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
    if n%2 == 0:
        tot = arr[int(n/2)]+arr[int((n/2)-1)]
        tot = tot/2
    else:
        tot = arr[math.floor(n/2)]
    return tot

print(median_(arr))

def mode_(arr):
    dict_ = {}
    mode = []
    idx_max=0
    for item in arr:
        if item in dict_.keys():
            val  = dict_[item]
            val += 1
            dict_[item]=val
        else:
            dict_[item]=1
    print (dict_)
    
    value=list(dict_.values())
    # print (value)
    for j in range(len(value)):
        if value[j]>value[idx_max]:
            idx_max=j
    highest = value[idx_max]
    for key in dict_:
        if dict_[key] == highest:
            mode.append(key)
    
    if len(mode) == len (dict_):
        mode=[]
    return mode



  

    



print(mode_(arr))