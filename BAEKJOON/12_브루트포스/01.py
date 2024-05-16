from itertools import combinations
n, m = map(int, input().split())
nums = list(map(int, input().split()))
results = 0

for cards in combinations(nums,3):
    if sum(cards) <= m:
        results = max(results,sum(cards))
print(results)