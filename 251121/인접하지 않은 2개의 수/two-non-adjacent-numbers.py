n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
# 최대 합 저장
maximum = 0

# 인접하지 않은 2개의 수 모든 조합 찾기 
for i in range(n):
    # 1가지 수 확정 
    num_sum = numbers[i]
    # 나머지 수 고르기 : 고른 수 이전에서 고르기 
    for j in range(i-1):
        num_sum += numbers[j]
        maximum = max(maximum, num_sum)
        num_sum = numbers[i]
    # 나머지 수 고르기: 고른 수 이후에서 고르기 
    for j in range(i+2, n):
        num_sum += numbers[j]
        maximum = max(maximum, num_sum)
        num_sum = numbers[i]

print(maximum)