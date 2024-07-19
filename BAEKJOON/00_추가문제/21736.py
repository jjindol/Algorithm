import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))

visited = [[False]*m for i in range(n)]

num = 0
def bfs(x,y):
    global num
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        if graph[x][y] == 'P':
            num += 1
        graph[x][y] = 'X'

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!='X':
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I' and not visited[i][j]:
            bfs(i,j)
            break

if num > 0:
    print(num)
else:
    print('TT')