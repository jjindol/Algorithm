arr = []
length = []

for _ in range(5):
    word = input()
    arr.append(word)
    length.append(len(word))
    
for i in range(max(length)):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')