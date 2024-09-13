from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
step = [[-1]*m for _ in range(n)]

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m and graph[x][y] == 1

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()

        dx,dy = [1,0,-1,0],[0,1,0,-1]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if in_range(nx,ny) and not visited[nx][ny]:
                push(nx,ny,step[x][y]+1)

push(0,0,0)
bfs()
print(step[n-1][m-1])