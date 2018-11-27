def fibo(n):
    fb=[]
    for i in range (n):
        if (i < 2):
            fb.append(1)
        else:    
            fb.append(fb[i-1]+fb[i-2])
    print(fb)

# fibo(6)

def fiborec(n):
    if n < 2:
        return 1
    else: 
        fiborec(n-1)

def fibonacci(number):
  if number < 2:
    return number
  else:
    return fibonacci(number - 1) + fibonacci(number - 2)

print (fibonacci(7))

