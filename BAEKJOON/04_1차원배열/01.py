n = int(input())
my_list = list(map(int, input().split()[:n]))

v = int(input())

count = my_list.count(v)

print(count)