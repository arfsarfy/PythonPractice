def fizzBuzz(n):
    a=''
    for i in range(1,n+1):
        if i%3 ==0:
            a = 'Fizz'
            if i%5 !=0:
                print(a)
        if i%5 == 0:
            print(a+ 'Buzz')
        if  i%5 != 0 and i%3 !=0:
            print(i) 
        a=''

i=0
x=int(input('Input a number: '))
z=''
fizzBuzz(x)