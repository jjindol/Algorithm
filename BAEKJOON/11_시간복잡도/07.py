a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

if (a1*n + a2) <= c*n and a1+ a2//n <= c:
    print(1)
else:
    print(0)