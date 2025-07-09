a, b = map(int, input().split())
n = input()

# Please write your code here.
# a진수 -> 10진수
n = int(n, a)

# 10진수 -> b진수
digits = []
 
while True:
    if n < b:
        digits.append(n)
        break
    digits.append(n % b)
    n //= b

for d in digits[::-1]:
    print(d, end='')