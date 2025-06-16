arr = [list(map(int, input().split())) for _ in range(2)]

# 행 평균
avr1 = round(sum(arr[0])/4, 1)
avr2 = round(sum(arr[1])/4, 1)
print(f"{avr1} {avr2}")

# 열 평균
for i in range(4):
    total = 0
    for j in range(2):
        total += arr[j][i]
    print(round(total/2, 1), end=' ')

# 전체 평균
avr = round((avr1+avr2)/2, 1)
print()
print(avr)
