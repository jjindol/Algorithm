#방법1: 내 코드
n = int(input())
lst = []
i = 0

while len(lst) < n:
    if '666' in str(i):
        lst.append(i)
    i += 1

print(lst[n-1])

#방법2: 개선된 코드
n = int(input())
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1
        if cnt == n:
            print(num)
            break
    num += 1