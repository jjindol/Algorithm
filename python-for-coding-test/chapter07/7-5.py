def binary_search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return False

n = int(input())
lst1 = list(map(int, input().split()))

m = int(input())
lst2 = list(map(int, input().split()))

for x in lst2:
    if binary_search(lst1, x):
        print("yes", end=' ')
    else:
        print("no", end=' ')


