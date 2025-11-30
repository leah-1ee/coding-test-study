N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 연속 T번 높이 H

# 최소 비용 저장 
min_cost = float('inf')

# 시작 위치 결정 
for i in range(len(arr)-T+1):
    cost = 0
    # i ~ i + T 순회, 높이 H 맞추기 위한 비용 계산 
    for j in range(i, i+T):
        cost += abs(arr[j]-H)
    # 최소 비용 업데이트 
    min_cost = min(min_cost, cost)

print(min_cost)