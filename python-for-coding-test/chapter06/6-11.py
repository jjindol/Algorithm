n = int(input())
lst = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    lst.append((name,score))

lst.sort(key=lambda x : (-x[1],x[0]))

for x in lst:
    print(x[0], end=' ')

#변형: score에 대해 내림차순, score가 같으면 name에 대해 오름차순