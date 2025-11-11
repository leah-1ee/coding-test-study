n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 2 ~ n-1 번째 체크포인트 건너뛰기 
min_dist = float('inf')

for i in range(1, n-1):
    # i 번째 건너뛰기 
    pass_point = points[:i] + points[i+1:]

    dist = 0
    # 거리 계산
    for j in range(n-2):
        x1, y1 = pass_point[j]
        x2, y2 = pass_point[j+1]
        dist = dist + abs(x1-x2) + abs(y1-y2)

    # 최소 거리 업데이트 
    min_dist = min(min_dist, dist)

print(min_dist)