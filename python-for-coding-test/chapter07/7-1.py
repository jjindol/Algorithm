def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 #현재 위치 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오.")
data = input().split()
n = int(data[0])
target = data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하시오. 구분은 띄어쓰기 한 칸으로 한다.")
array = input().split()

print(sequential_search(n,target,array))
print("순차 탐색의 시간 복잡도는 최악의 경우 O(N)")