n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def func(arr):
    tmp = 1
    ans = 0
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            tmp += 1
        else:
            tmp = 1
        if tmp >= m:
            ans += 1
            break
    return ans

if n==1 and m==1:
    print(2)
else:
    cnt1 = 0
    for i in range(n):
        cnt1 += func(graph[i])  # 각 행에 대해 func 호출

    cnt2 = 0
    for j in range(n):
        col = [graph[i][j] for i in range(n)]  # 각 열을 별도로 추출
        cnt2 += func(col)  # 각 열에 대해 func 호출

    print(cnt1 + cnt2)