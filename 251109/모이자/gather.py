import sys 

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
INT_MAX = sys.maxsize
min_sum = INT_MAX

# 완전탐색 
for i in range(n):
    # 반복 합 
    total = 0

    for j in range(n):
        # 명 수 * 거리 
        if i >= j:
            total += A[j] * (i-j)
        else:
            total += A[j] * (j-i)

    # 최소 거리 업데이트 
    min_sum = min(min_sum, total)

print(min_sum)
    