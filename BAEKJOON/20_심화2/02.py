def func(n):
    s = set()
    cnt = 0

    for _ in range(n):
        word = input()
        if word != "ENTER":
            if word not in s:
                cnt += 1
                s.add(word)
        else:
            s.clear()
    return cnt

N = int(input())
print(func(N))