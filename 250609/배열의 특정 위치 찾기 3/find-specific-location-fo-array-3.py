lst = list(map(int, input().split()))
arr = []

# 0 입력 전까지 arr에 추가 
for i in lst:
    if i != 0:
        arr.append(i)
    else:
        break

# 끝 3개 정수 더하기 
print(arr[-1]+arr[-2]+arr[-3])