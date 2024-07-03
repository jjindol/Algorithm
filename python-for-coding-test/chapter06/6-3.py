#특정한 데이터를 적절한 위치에 삽입

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)