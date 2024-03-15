word = input().strip()

# 알파벳 a부터 z까지의 위치를 저장할 리스트를 -1로 초기화
positions = [-1] * 26

for i in range(len(word)):
    # 알파벳의 인덱스를 구함
    index = ord(word[i]) - ord('a')
    # 해당 알파벳이 처음 등장하는 위치를 저장
    if positions[index] == -1:
        positions[index] = i

# 결과 출력
for pos in positions:
    print(pos, end=' ')
