n = int(input())
lst1 = list(map(int, input().split()))

m = int(input())
lst2 = list(map(int, input().split()))

count = dict()
for num in lst1:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

result = []
for num in lst2:
    result.append(count.get(num, 0))

print(' '.join(map(str, result)))

'''
key: lst2 내의 숫자
value: 그 숫자의 개수
lst1가 [1, 2, 3, 2, 1]인 경우, count는 {1: 2, 2: 2, 3: 1}
'''