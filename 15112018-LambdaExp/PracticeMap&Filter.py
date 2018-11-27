#Map
def mapf(fn,x):
    newlist = []
    for item in x:
        # y= fn(item)
        newlist.append(fn(item))
    return newlist

def satu(num):
    return "kita ber" +str(num*3)
listNum = [1,2,3,4,5]
New_map = list(mapf(satu,listNum))
# print(New_map)

#Filter
def filterf(fn,x):
    newlist = []
    for item in x:
        if fn(item):
            newlist.append(item)
    return newlist

stuff = ['Merdeka','Hello','Hellos','Sohib','Kari Ayam']
print(stuff)
input_ = input('Search :') 

out = list(filterf(lambda x: input_ in x.lower(),stuff))
print(out)
