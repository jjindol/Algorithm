t = int(input())

for _ in range(t):
    x = int(input())
    a = x//25
    b = x%25 // 10
    c = (x%25 % 10) // 5
    d = (x%25 % 10) % 5
    print(a,b,c,d)

#다른 풀이
t = int(input())

for _ in  range(t):
    x = int(input())
    arr = []
    for i in [25, 10, 5, 1]:
        arr.append(x // i)
        x = x % i
    print(*arr)