lst = list(map(int, input().split()))
arr = []

# 3의 배수 나올 때까지 배열에 추가 
for n in lst:
    if n % 3 != 0:
        arr.append(n)
    else:
        break

# 마지막 원소 출력 
print(arr[-1])