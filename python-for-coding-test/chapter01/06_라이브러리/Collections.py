from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.appendleft(0)
data.append(5)
data.popleft()
print(list(data))


from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))