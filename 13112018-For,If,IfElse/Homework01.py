x= input('input a number: ')
x=int(x)

# if (x%2==0):
#     print('Angka',x,'tergolong Genap')
# else:
#     print('Angka',x,'tergolong Ganjil')

###More efficient
array = ['Genap','Ganjil']
print ('Angka {} tergolong bilangan {}'.format(x,array[x%2]))