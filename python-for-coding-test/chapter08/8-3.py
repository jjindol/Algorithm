#호출되는 함수 확인

d = [0] * 100

def fibo(n):
    print(str(n), end=' ')
    
    if n==1 or n==2:
        return 1
    
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    
    return d[n]

    
fibo(6)