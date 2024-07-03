#빈 리스트 선언
a = list()
b = []

print(a)
print(b)


#리스트 인덱싱: 인덱스 값을 입력하여 특정 원소에 접근
a = [1,2,3,4,5,6,7,8,9]
#뒤에서 첫 번째 원소 출력
print(a[-1])

#뒤에서 세 번째 원소 출력
print(a[-3])

#네 번째 원소 값 변경
a[3] = 0
print(a)


#리스트 슬라이싱: 연속적인 위치를 갖는 원소들을 가져옴
b = [1,2,3,4,5,6,7,8,9]

print(b[1:4])


#리스트 컴프리헨션
array = [x for x in range(20) if x%2==1]
print(array)


#N x M 크기의 2차원 배열 초기화
n=3
m=4
array = [[0]*m for _ in range(n)]
for arr in array:
    print(arr, sep=' ')


#리스트에서 특정한 값의 원소를 모두 제거하려면?
arr = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in arr if i not in remove_set]
print(result)