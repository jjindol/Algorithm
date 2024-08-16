n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(n-2):
        result = max(result, lst[i][j]+lst[i][j+1]+lst[i][j+2])

print(result)