def dfs(x,y,num):
    if len(num) == 6:
        result.append(num)
        return
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        else:
            dfs(nx, ny, num + graph[nx][ny])
    
result = []
graph = []

for _ in range(5):
    graph.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
        
print(len(set(result)))