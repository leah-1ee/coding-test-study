N = input()

# Please write your code here.
# 2진수 -> 10진수
num = 0

for i in N:
    num = num * 2 + int(i)

# 17배
num *= 17

# 10진수 -> 2진수 
digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num % 2)
    num //= 2

for d in digits[::-1]:
    print(d, end='')