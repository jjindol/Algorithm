#itertools 라이브러리
from itertools import permutations, combinations, product

data = ['A', 'B', 'C']
result1 = list(permutations(data, 3))
result2 = list(combinations(data, 2))
result3 = list(product(data, repeat=2))
print(result1)
print(result2)
print(result3)