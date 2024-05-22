n,m = map(int, input().split())
my_set = set()
lst = []

for _ in range(n):
    word = input()
    my_set.add(word)

for _ in range(m):
    word_test = input()
    lst.append(word_test)

count = 0
for word_test in lst:
    if word_test in my_set:
        count += 1
print(count)

"""
N개의 집합에 대해 M개의 입력 중 몇 개가 N개에 속하는 지 구하는 문제로 N개는 집합으로 중복된 것이 있을 수 없지만 입력 M에 대해서는 중복이 있을 수 있기에 같은 것이 입력되면 그 만큼 정답의 개수에 추가에 주어야 합니다. 따라서 코드에서 b를 set으로 선언하신 것은 올바르지 않은 방법입니다.
"""