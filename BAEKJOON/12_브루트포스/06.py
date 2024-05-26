n = int(input())
lst = []

for i in range(n//3+1):
    for j in range(n//5+1):
        if 3*i + 5*j == n:
            lst.append((i,j))

if lst:
    print(min(i + j for i, j in lst))
else:
    print(-1)

#if lst: 리스트가 비어 있지 않은 경우 = 해가 있는 경우