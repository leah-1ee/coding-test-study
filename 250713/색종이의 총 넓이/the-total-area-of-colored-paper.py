n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# 음수 좌표 방지 오프셋 
offset = 100
# 좌표평면 0으로 초기화
plane = [[0 for _ in range(201)] for _ in range(201)]

# 사각형 1로 채우기 
for i in range(n):
    for j in range(x[i] + offset, x[i] + offset + 8):
        for k in range(y[i] + offset, y[i] + offset + 8):
            plane[k][j] = 1

total = sum(sum(row) for row in plane)
print(total)