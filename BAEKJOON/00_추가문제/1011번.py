t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    distance = y-x
    move = 0 #이동 거리
    result = 0 #이동 횟수
    cnt = 0 #반복 횟수

    while move < distance:
        result += 1
        if result % 2 != 0:
            cnt += 1
        move += cnt
    print(result)