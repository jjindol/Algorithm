import sys

n,m = map(int, sys.stdin.readline().split())
num = [0] * n
print(num)

for _ in range(m):
    i,j,k = map(int, sys.stdin.readline().split())
    num[i-1:j] = [k] * (j-i+1)

print(*num)


# 확인!!