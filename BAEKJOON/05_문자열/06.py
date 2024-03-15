word = input()
alphabet = [chr(j) for j in range(97,123)]

for x in alphabet:
    print(word.find(x), end=' ')