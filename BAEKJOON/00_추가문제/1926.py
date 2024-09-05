from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
step = [[0] * m for _ in range(n)]
q = deque()

dx,dy = [1,0,-1,0], [0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    cnt = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += 1
                push(nx,ny,step[x][y]+1)
    return cnt


lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            push(i,j,1)
            lst.append(bfs())

if len(lst) == 0:
    print(0)
    print(0)
else:   

    print(len(lst))
    print(max(lst))