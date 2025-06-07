# 입력 받는 리스트 
lst = list(map(int, input().split()))

total = num = 0

# 0 나오면 종료, 2의 배수 나오면 개수+1, 합계에 더함 
for n in lst:
    if n == 0:
        break
    elif n % 2 == 0:
        total += n
        num += 1

# 출력 
print(num, end = ' ')
print(total)
