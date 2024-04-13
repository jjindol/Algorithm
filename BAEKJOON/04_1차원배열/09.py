import sys
num = []
n,m = map(int, input().split())

for i in range(n):
    num.append(i+1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    num[i-1:j] = reversed(num[i-1:j])

print(*num)