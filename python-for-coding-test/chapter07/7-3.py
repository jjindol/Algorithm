def binary_search(array, target):
    array.sort()
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print('원소는' , result , '번 인덱스에 위치')