n = int(input())
lst = list(map(int, input().split()))

# 리스트 정렬 
lst.sort()

min_diff = float('inf')

# 차이 계산, 업데이트 
for i in range(n-1):
    diff = abs(lst[i]-lst[i+1])

    if diff != 0:
        min_diff = min(diff, min_diff)

print(min_diff)