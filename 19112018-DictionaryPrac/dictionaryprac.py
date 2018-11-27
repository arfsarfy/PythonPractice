def lihatdict(dict_):
    k = 'Key'
    k = k.center(24)
    v = 'Value' 
    v = v.center(24)
    print(k + '|' + v)
    print('_________________________________________________\n')
    for key_,val in dict_.items():
        key_=str(key_).center(24)
        if type(val) is str:
            val = "'"+val+"'"
        val =str(val).center(24)
        print(key_+"|"+val)
    print('\n')
    n = input('Masukan 0 untuk kembali ke Menu Awal :')
    if n == '0':
        dict_pract()
    else:
        lihatdict(dict_)


def isidict(dict_):
    
    print ('Isi Dictionary Menu\n')
    k = input('Masukkan nama untuk Key dictionary :')
    # v = input('Masukkan Value nya :')
    while True:
        n = input('Ketik 1 masukkan integer; 0 untuk string :')
        if n == '1':
            dict_[k]=int(input('Masukkan Integer Value nya :'))
            break
        elif n == '0':
            dict_[k]=input('Masukkan String Value nya :')
            break

    x = input ('\n1 untuk isi dictionary; 0 untuk kembali ke Menu Awal :')
    if x == '1':
        isidict(dict_)
    elif x == '0':
        dict_pract()
    else:
        print ('error. kembali ke menu awal')
        dict_pract()


def searchdict(dict_):
    search = input('Search key in the dictionary :')
    k = 'Key'
    k = k.center(24)
    v = 'Value' 
    v = v.center(24)
    print(k + '|' + v)
    print('_________________________________________________\n')
    out = filter(lambda x: search.lower() in x.lower(),dict_)
    for keys in out:
        value = dict_.get(keys)
        keys=str(keys).center(24)
        if type(value) is str:
            value = "'"+value+"'"
        value =str(value).center(24)
        print(keys + "|" + value)
    print('\n')

    n = input('Masukkan 1 untuk mencari lagi; Masukan 0 untuk kembali ke Menu Awal :')
    if n == '0':
        dict_pract()
    elif n == '1':
        searchdict(dict_)
    else:
        print('Error. Kembali ke menu awal.')
        dict_pract()
        
def dict_pract():
    while True:
        print('Main Menu:\n1.Lihat Dictionary\n2.Isi Dictionary\n3.Search Dictionary\n4.Keluar\n')
        n =input('Pilih Menu :')
        if n =='1':
            lihatdict(thedictionary)
            break
        elif n =='2':
            isidict(thedictionary)
            break
        elif n =='3':
            searchdict(thedictionary)
            break
        elif n =='4':
            print('Program End. Thank You')
            break

thedictionary={}
dict_pract()