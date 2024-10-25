n,m = map(int, input().split())
lst = [0] * (n+1)

for _ in range(m):
    x,y,z= map(int,input().split())
    for i in range(x,y+1):
        lst[i] = z
        
for i in range(1,n+1):
    print(lst[i], end=' ')