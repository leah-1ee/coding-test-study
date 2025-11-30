N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 연속 T번 높이 H


min_cost = float('inf')

for i in range(len(arr)-T):
    cost = 0
    for j in range(i, i+T):
        cost += abs(arr[j]-H)
    min_cost = min(min_cost, cost)

print(min_cost)