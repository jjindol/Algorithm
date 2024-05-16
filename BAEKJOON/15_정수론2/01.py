#풀이1: 시간초과 코드
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    tmp = 1
    lst = []
    while tmp <= x and tmp <= y:
        if x % tmp == 0 and y % tmp == 0:
            lst.append(tmp)
        tmp += 1
    G = max(lst)
    L = G * (x // G) * (y // G)

    if len(lst) == 1:
        print(x * y)
    else:
        print(L)

#풀이2
import math
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    print(abs(x*y)//math.gcd(x,y))

#최대공약수: G, 최소공배수:L