word = input()
keys = sorted(list(set(word)))
d = dict()
odd = []

for key in keys:
    cnt = word.count(key)
    d[key] = cnt
    if cnt % 2 == 1:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")

else:
    result = ''

    for key in keys:
        result += key * (d[key] // 2)

    if odd:
        result += odd[0] + result[::-1]
    else:
        result += result[::-1]
    print(result)