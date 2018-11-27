import math
x=input('Input days:')
x=int(x)

year = math.floor(x/360)
months = math.floor((x%360)/30)
weeks = math.floor(((x%360)%30)/7)
days  =math.floor(((x%360)%30)%7)

print ("it's equal to",year,'year/s',months,'month/s',days,'day/s')



