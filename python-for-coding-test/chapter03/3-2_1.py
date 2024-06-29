n, m, k = map(int, input().split())

num = list(map(int, input().split()))


first_num = max(num)
num.remove(first_num)
second_num = max(num)


# 최댓값의 개수를 셈
cnt = num.count(first_num)

tmp = m // (k + 1)
remainder = m % (k + 1)

# cnt가 2 이상이고, 해당 조건을 만족하는 값이 배열 내에서 가장 큰 값인지 확인
if cnt >= 2:
    result = first_num * m
else:
    result = (first_num * k + second_num) * tmp + first_num * remainder

print(result)