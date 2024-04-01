import sys
input = sys.stdin.readline
n,m = map(int, input().split())

arr1 = []
for _ in range(m):
    arr1.append(list(map(int, input().split())))

arr2 = []
for _ in range(m):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end=' ')
    print()