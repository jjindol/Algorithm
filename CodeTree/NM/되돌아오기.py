n = int(input())

dx,dy = [1,0,0,-1],[0,-1,1,0]
directions = {'E':2, 'S':0, 'W':1, 'N':3}


def func():
    x,y = 0,0
    cnt = 0

    for _ in range(n):
        a,b = input().split()
        b = int(b)
        dir = directions[a]

        for _ in range(b):
            nx,ny = x+dx[dir],y+dy[dir]

            if nx==0 and ny==0:
                print(nx,ny)
                cnt += 1
                return cnt
            
            else:
                x,y = nx,ny
                print(nx,ny)
                cnt += 1          

    return -1

print(func())
