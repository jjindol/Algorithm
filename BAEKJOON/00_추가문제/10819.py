from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
lst = []

def func(arr, idx):
    if idx == len(arr) -1:
        return 0
    return abs(arr[idx]-arr[idx+1]) + func(arr, idx+1)

for perm in permutations(arr):
    lst.append(func(perm, 0))

print(max(set(lst)))