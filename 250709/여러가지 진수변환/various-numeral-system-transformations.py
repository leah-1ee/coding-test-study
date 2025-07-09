N, B = map(int, input().split())

# Please write your code here.
digits = []

# 4진수 변환 
if B == 4:
    while True:
        if N < 4:
            digits.append(N)
            break
        digits.append(N % 4)
        N //= 4

# 8진수 변환 
elif B == 8:
    while True:
        if N < 8:
            digits.append(N)
            break
        digits.append(N % 8)
        N //= 8

for d in digits[::-1]:
    print(d, end='')