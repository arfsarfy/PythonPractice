Dictionary ={'arfy':{'lalala':'lolo'},'ganteng':'iya'}

print(Dictionary.keys())
print (list(Dictionary.keys()))

for keys in Dictionary.keys():
    print(Dictionary[keys])

arr = [1,2,3,1,1,1,3,25,6]
s =set(arr)

print (s)

def satu(num):
    return "kita ber" +str(num*3)

#the list
listNum = [1,2,3,4,5]

#list comprehension
New = [satu(item) for item in listNum]

#method below is similar to above#

#Map
New_map = list(map(satu,listNum))
print(New)
print(New_map)


#Buat function seperti fn map & filter#