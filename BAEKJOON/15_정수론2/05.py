def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    while not isPrime(n):
        n += 1
    print(n)