n, m = map(int, input().split())
lst = []

for _ in range(n):
    row = list(map(int, input().split()))
    
    M = min(row)
    lst.append(M)
print(max(lst))