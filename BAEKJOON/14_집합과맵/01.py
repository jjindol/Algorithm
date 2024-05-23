#풀이1
s = set()
lst = []

n = int(input())
s.update(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)):
    if lst[i] in s:
        lst[i] = 1
    elif lst[i] not in s:
        lst[i] = 0
print(*lst)



#풀이2
import sys
input = sys.stdin.readline

def binary_search(array, check, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == check:
            return True
        elif array[mid] > check:
            end = mid - 1
        else:
            start = mid + 1
    return False

N = int(input())
your_card = sorted(list(map(int, input().rstrip().split())))

M = int(input())
compare_card = list(map(int, input().rstrip().split()))

for num in compare_card:
    if binary_search(your_card, num, 0, N-1):
        print(1, end=' ')
    else:
        print(0, end=' ')