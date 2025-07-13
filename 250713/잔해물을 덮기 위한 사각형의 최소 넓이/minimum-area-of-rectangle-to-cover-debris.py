x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
# 음수 좌표 방지 인덱스
offset = 1000

# 좌표평면 0으로 초기화
plane = [[0 for _ in range(2001)] for _ in range(2001)]

# 첫 번째 정사각형 1로 채우기
for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        plane[j][i] = 1

# 두 번째 정사각형 0으로 덮기
for i in range(x1[1] + offset, x2[1] + offset):
    for j in range(y1[1] + offset, y2[1] + offset):
        plane[j][i] = 0

# 남은 부분 중 최대 행, 열 길이 구하기 
max_width = max(sum(row) for row in plane)
max_height = max(sum(col) for col in zip(*plane))

# 넓이 
print(max_width * max_height)