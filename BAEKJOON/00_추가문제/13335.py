from collections import deque

n,w,L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
time = 0

while trucks or sum(bridge) > 0:
    time += 1
    bridge.popleft()

    if trucks:
        if trucks[0] + sum(bridge) <= L:
            t = trucks.popleft()
            bridge.append(t)

        else:
            bridge.append(0)

print(time)