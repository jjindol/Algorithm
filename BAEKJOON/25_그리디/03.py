n = int(input())
P = list(map(int, input().split()))
P.sort()

tmp = 0
arr = []

for i in range(n):
    tmp += P[i]
    arr.append(tmp)

print(sum(arr))