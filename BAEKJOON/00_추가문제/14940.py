from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]

q = deque()

def can_go(x,y):
    return 0<=x<n and 0<=y<m and graph[x][y] == 1

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if can_go(nx,ny) and not visited[nx][ny]:
                push(nx,ny,step[x][y]+1)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            push(i,j,0)

        elif graph[i][j] == 1 and step[i][j] == 0:
            step[i][j] = -1
bfs()
for x in step:
    print(" ".join(map(str,x)))