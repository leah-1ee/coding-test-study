x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
# 음수 좌표 방지
offset = 1000
# 전체 좌표 생성, 0으로 초기화 
plane = [[0 for _ in range(2001)] for _ in range(2001)]

# 사각형 A, B 1로 채우기
for i in range(2):
    for j in range(x1[i] + offset, x2[i] + offset):
        for k in range(y1[i], y2[i]):
            plane[k][j] = 1

# M으로 덮이는 부분 0으로
for j in range(x1[2] + offset, x2[2] + offset):
    for k in range(y1[2], y2[2]):
        plane[k][j] = 0

total = sum(sum(row) for row in plane)
print(total)
