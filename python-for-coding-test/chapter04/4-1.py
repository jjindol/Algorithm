n = int(input())
x,y = 1,1
plans = input().split()

#L,R,U,D에 따른 이동 방향
dx,dy = [0,0,-1,1], [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx,ny = x+dx[i], y+dy[i]

    if nx < 1 or ny < 1 or nx > n or  ny > n:
        continue

    x,y = nx,ny

print(x,y)