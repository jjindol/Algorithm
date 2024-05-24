#풀이1
import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n):
    a,b = map(str, input().split())
    if b == "enter":
        s.add(a)
    elif b == "leave":
        s.remove(a)

for person in sorted(s, reverse=True):
    print(person)


#풀이2
import sys
input = sys.stdin.readline
n = int(input())
company = {}

for _ in range(n):
    man, state = input().rstrip().split()
    if state == 'enter':
        company[man] = True
    else:
        del company[man]

print("\n".join(sorted(company.keys(), reverse=True)))