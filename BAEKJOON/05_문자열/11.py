import sys
count = 0

while True:
    word = sys.stdin.readline().strip()
    print(word)
    count += 1
    if count > 100:
        break