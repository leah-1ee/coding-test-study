n = int(input())
lst = list(map(int, input().split()))
arr = []

# 짝수면 arr에 추가
for num in lst:
    if num % 2 == 0:
        arr.append(num)

# 거꾸로 출력 
for num in arr[::-1]:
    print(num, end = ' ')