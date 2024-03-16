#N*M 크기의 2차원 배열 초기화: 리스트 컴프리헨션 이용
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

a = [1,4,3]
print("기본 리스트: " , a)

a.append(2)
print("삽입: " , a)

a.sort()
print("오름차순 정렬: " , a)

a.sort(reverse=True)
print("내림차순 정렬: " , a)

a.reverse()
print("원소 뒤집기: " , a)

a.insert(2,3)
print("인덱스 2에 3 추가: " , a)

print("특정 값(3) 데이터 세기: " , a.count(3))

a.remove(2)
print("값이 2인 데이터 삭제: " , a)