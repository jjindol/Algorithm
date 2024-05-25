import math, sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

if math.gcd((a*d) + (b*c),(b*d)) == 1:
    A = a*d + b*c
    B = b*d
    print(A,B)
else:
    C = ((a*d) + (b*c)) // math.gcd(a*d + b*c, b*d)
    D = b*d // math.gcd(a*d + b*c, b*d)
    print(C,D)