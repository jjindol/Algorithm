n = int(input())
x = 0

for i in range(1,n+1):
    num = list(map(int, str(i)))
    x = sum(num) + i
    if x == n:
        print(i)
        break
    elif i == n:
        print(0)