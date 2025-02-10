n,m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

answer_B = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
answer_W = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']

def func(graph):
    cnt1,cnt2 = 0,0

    for i in range(8):
        for j in range(8):
            if graph[i][j] != answer_B[i][j]:
                cnt1 += 1
            if graph[i][j] != answer_W[i][j]:
                cnt2 += 1
    return min(cnt1,cnt2)

result = 2500
for i in range(n-7):
    for j in range(m-7):
        new = [row[j:j+8] for row in arr[i:i+8]]
        result = min(result, func(new))

print(result)