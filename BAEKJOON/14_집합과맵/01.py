#풀이1
import sys
input = sys.stdin.readline

n = int(input())
my_card = set(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

for x in range(m):
    if card[x] in my_card:
        print(1, end=' ')
    else:
        print(0, end=' ')


'''
풀이2
import sys

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

#풀이3
input = sys.stdin.readline

N = int(input())
your_card = sorted(list(map(int, input().rstrip().split())))

M = int(input())
compare_card = list(map(int, input().rstrip().split()))

for num in compare_card:
    if binary_search(your_card, num, 0, N-1):
        print(1, end=' ')
    else:
        print(0, end=' ')
'''