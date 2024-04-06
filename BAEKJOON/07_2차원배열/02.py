import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

max_value = max(map(max, arr))
print(max_value)

found = False
for i in range(9):
    for j in range(9):
        if arr[i][j] == max_value:
            if not found:
                print(i + 1, j + 1)
                found = True