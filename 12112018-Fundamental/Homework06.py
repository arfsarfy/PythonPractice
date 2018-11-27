import math
dis = 120
a = 60
b = 40
x=(120/(a+b))*3600
# print(x)
time_h=9
time_min=00
time_sec=00

hour   = math.floor(x/3600)
minute = math.floor((x%3600)/60)
second = math.floor((x%3600)%60)

time_h+=hour
time_min+=minute
time_sec+=second
# print(time_min)

print ('The cars will crash at '+str(time_h)+':'+str(time_min)+':'+str(time_sec))