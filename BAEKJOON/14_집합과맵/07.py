a,b = map(int, input().split())

set1 = set()
set2 = set()

set1.update(map(int, input().split()))
set2.update(map(int, input().split()))

union = set1 | set2
intersection = set1 & set2
result = union - intersection

print(len(result))