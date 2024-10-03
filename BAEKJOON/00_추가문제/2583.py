import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    if graph[y][x] == 1:
        return 0
    
    graph[y][x] = 1
    count = 1 #현재 영역의 크기

    count += DFS(x-1, y)
    count += DFS(x+1, y)
    count += DFS(x, y-1)
    count += DFS(x, y+1)
    
    return count

answer = 0 #영역의 개수
result = []

for i in range(n):
    for j in range(m):
        if graph[j][i] == 0:
            count = DFS(i, j)
            result.append(count)
            answer += 1
result.sort()
print(answer)
print(' '.join(map(str, result)))