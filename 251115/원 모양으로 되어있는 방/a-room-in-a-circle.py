n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 최소 거리 저장 
min_dist = float('inf')

# i번 방에서 시작한다고 가정
for i in range(n):
    # 거리 저장 
    dist = 0
    
    # 거리 합 계산 
    for j in range(n):

        # 한 바퀴 돌아야 하는 경우 (n -> 1 이동 있음)
        if j < i:
            dist += abs(n-j-1) * a[j]
        # 돌지 않아도 됨 
        else:
            dist += abs(i-j) * a[j]

    # 최솟값 업데이트 
    min_dist = min(min_dist, dist)


print(min_dist)