def fibonacci_generator():
    a=b=1
    print('series:')
    while True:
        yield a
        a,b=b,a+b
fib=fibonacci_generator()
for i in fib:
            if i > 100:
                break
            else:
                print('generated:',i)
        
