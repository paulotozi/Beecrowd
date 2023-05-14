N = int(input())
for i in range(N):
    
    num = int(input())
    fib = [0,1]
    if(num > 1):
        
        for j in range(2, num + 1):
           
            fib.append(fib[j - 2] + fib[j - 1])

        print('Fib({}) = {}'.format(num, fib[num]))
    
    if(num <= 1):

        print('Fib({}) = {}'.format(num, fib[num]))
