from collections import deque

#n,m을 공백으로 구분해 입력받기
n,m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네 방향 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]
#bfs 코드 구현
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x,y))

    #큐가 빌 때까지 반복
    while q:
        (x,y) = q.popleft()

        #현재 위치에서 4방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            #괴물을 마추친 경우 무시
            if graph[nx][ny] == 0:
                continue

            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

    #우측 하단까지의 최단 거리 반환
    return graph[n-1][m-1]

#bfs 수행결과 출력
print(bfs(0,0))