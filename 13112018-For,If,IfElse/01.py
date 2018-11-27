arr=['man',['i','am'],'bored']

for item in arr:
    if(type(item) == type(' ')):
        print(item)
    elif(type(item) == type([])):
        for n in item:
            print(n)