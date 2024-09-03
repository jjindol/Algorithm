from collections import deque

n = int(input())
r1,c1, r2,c2 = map(int, input().split())
q = deque()

visited = [[False]*n for _ in range(n)]
step = [[-1]*n for _ in range(n)]

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]

            if in_range(nx,ny) and not visited[nx][ny]:
                push(nx,ny,step[x][y]+1)


push(r1-1, c1-1, 0)
bfs()
print(step[r2-1][c2-1])