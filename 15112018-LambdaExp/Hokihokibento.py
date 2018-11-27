def choices(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n==4:
        return 4            
    else:
        return 0  

def cart():
    print('Isi Cart :')
    for paket,quan in incart.items():
        price = menu.get(paket)
        print(paket,"   Rp.",price, "  Jumlah: ", quan)
    user_input=int(input('Masukkan 0 untuk kembali ke menu awal :'))
    if user_input == 0:
        hokihokibento()
    else:
        cart()

def checkout():
    print('Checkout')
    z=''
    totalprice=0
    for paket,quan in incart.items():
        price = menu.get(paket)
        z+= str(paket) + "  price @ : Rp." + str(price) +" x " + str(quan) + '\n'
        totalprice += int(price) * int(quan)
    print(z)
    print('Harga Total = Rp.',totalprice)
    user_in=int(input('\nKetik 1 untuk pembayaran; 0 untuk kembali ke menu utama:'))
    if user_in == 1:
        while True:
            uang = int(input('Jumlah uang anda = Rp.'))
            if uang >= totalprice:
                change = uang- totalprice
                print ('kembalian anda   = Rp.'+ str(change)+ "\n Terima Kasih!")
                break
            else:
                print('Maaf uang anda kurang.')
            hokihokibento()
    elif user_in == 0:
        hokihokibento()
    else:
        checkout()

def UI_(num):
    UI= {1:menuF,2:cart,3:checkout,4:exit}
    # print('iam here')
    if num == 0:
        hokihokibento()
    else:
        UI[num]()

def addtocart():
    user_input2=int(input('Masukkan angka untuk pesan; ketik 0 untuk kembali ke menu utama:'))
    if user_input2 == 0:
        hokihokibento()
    elif user_input2 >=1 and user_input2 <=3:    
        menu_arr=list(menu.keys())
        # print(menu_arr)
        chosen = choices(user_input2-1)
        print(menu_arr[chosen])
        quantity =int(input('Quantity:'))
        incart[menu_arr[chosen]]=quantity
        hokihokibento()
    else:
        menuF()

def menuF():
    print('\nSilahkan pilih pesanan anda')
    for paket,price in menu.items():
        print(paket, "   Rp.", price)
    addtocart()
    
def hokihokibento():
    print('Main Menu:\n1.Lihat Menu\n2.Lihat Cart\n3.Checkout\n4.Keluar\n')
    user_input=int(input('Masukkan angka:'))
    UI_(choices(user_input))

#global variable
menu={'1.Paket A':35000,'2.Paket B':25000,'3.Paket C':40000}
incart={}
#start program
hokihokibento()

#Too scketchy make simpler one
