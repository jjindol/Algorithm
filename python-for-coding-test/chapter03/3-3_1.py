n,m = map(int,input().split())

lst = []
for i in range(n):
    arr = list(map(int, input().split()))
    lst.append(min(arr))

print(max(lst))