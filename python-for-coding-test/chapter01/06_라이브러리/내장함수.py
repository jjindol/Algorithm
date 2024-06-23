#sorted(): iterable 객체에 대해 정렬된 결과 반환
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)


#튜플의 정렬은 key 속성을 이용해 명시
result1 = sorted([('A', 35), ('B', 75), ('C', 50)], key = lambda x: x[0], reverse=False) #key 기준 정렬
result2 = sorted([('A', 35), ('B', 75), ('C', 50)], key = lambda x: x[1], reverse=False) #value 기준 정렬
print(result1)
print(result2)