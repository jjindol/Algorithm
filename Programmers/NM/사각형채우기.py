n,m = map(int, input().split())

graph = [[0]*m for _ in range(n)]

dx,dy = [0,1,0,-1],[1,0,-1,0]
dir = 0
x,y = 0,0

arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def in_range(x,y):
    return 0<=x<n and 0<=y<m


graph[x][y] = 'A'
for i in range(2,n*m+1):
    nx,ny = x+dx[dir],y+dy[dir]

    if not in_range(nx,ny) or graph[nx][ny]!=0:
        dir = (dir+1)%4
        

    x,y = x+dx[dir],y+dy[dir]
    graph[x][y] = arr[(i-1)%26]


for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()