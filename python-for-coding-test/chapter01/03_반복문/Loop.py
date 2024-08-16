#while문
arr = [1, 2, 3, 4]
i = 0
lst = []

while True:
    lst.append(arr[i])
    
    i += 1
    
    if i >= len(arr):
        break

result = ''.join(map(str, lst))
print(result)  # 출력: "1234"


#for문
scores = [90, 85, 77, 65, 97]
cheating_list = {2,4}

for i in range(1,6):
    if i in cheating_list:
        continue
    if scores[i-1] >= 80:
        print(i, "번 학생: fail")