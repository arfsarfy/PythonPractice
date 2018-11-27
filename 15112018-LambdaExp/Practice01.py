stuff = ['Merdeka','Hello','Hellos','Sohib','Kari Ayam']
print(stuff)
input_ = input('Search :') 

def search(x=str):
    return input_ in x.lower()

out = list(filter(lambda x: input_.lower() in x.lower(),stuff))
# out = list(filter (search,stuff))
print(out)