a, b = map(int, input().split())

# a의 0번째와 2번째 자릿수를 바꾸기
a = int(str(a)[2] + str(a)[1] + str(a)[0])

# b의 0번째와 2번째 자릿수를 바꾸기
b = int(str(b)[2] + str(b)[1] + str(b)[0])

print(max(a, b))
