n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
max_num = arr[-1]
next_num = arr[-2]
tmp = m//(k+1)

answer = max_num*(m-tmp) + next_num*tmp
print(answer)