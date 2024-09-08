from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()

dx,dy = [1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if in_range(nx,ny):
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx,ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer,cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

answer = 0
makeWall(0)
print(answer)