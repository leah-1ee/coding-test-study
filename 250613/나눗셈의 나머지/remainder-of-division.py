a, b = map(int, input().split())
arr = [0]* 10

# 나머지 계산, 배열에 카운트
while a>1:
    left = a % b
    a //= b

    arr[left] += 1


# 제곱 합 출력 
arr = [x**2 for x in arr]
print(sum(arr))