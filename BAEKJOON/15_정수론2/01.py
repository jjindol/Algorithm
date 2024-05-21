#풀이1

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    gcd = 1
    for i in range(2, min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd = i
    result = gcd * (x//gcd) * (y//gcd)
    print(result)

#풀이2
import math
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    print(abs(x*y)//math.gcd(x,y))

#최대공약수(GCD) 최소공배수(LCM)