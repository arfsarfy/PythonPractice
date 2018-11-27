weight = input('Input your weight in kg:')
height = input('Input your height in cm:')
weight =int(weight)
height =int(height)

imt = weight/((height/100)**2)

if (imt<18.5):
    text = 'Berat badan kurang'
elif(imt>=18.5 and imt<25):
    text = 'Berat badan ideal'
elif(imt>=25 and imt<30):
    text = 'Berat badan berlebih'
elif(imt>=30 and imt<40):
    text = 'Berat badan sangat berlebih'
else:
    text ='Obesitas'

print('IMT =',imt,text)