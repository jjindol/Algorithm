#풀이1
a = int(input())
b = int(input())

b_hundreds = (b // 100)
b_tens = ((b % 100) // 10)
b_ones = (b % 10)

print(a * b_ones)
print(a * b_tens)
print(a * b_hundreds)
print(a*b)

# 풀이2
c = int(input())
d = input()

B = list(map(int,d))
I,J,K = c * B[-1], c * B[-2], c * B[-3]
print(I)
print(J)
print(K)
print(c * int(d))