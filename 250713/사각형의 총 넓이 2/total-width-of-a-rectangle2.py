n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
# 음수 좌표 방지 오프셋 설정
offset = 100

# 전체 평면 생성
plane = [[0 for _ in range(201)] for _ in range(201)]

# 사각형 칠하기 
for i in range(n):
    for j in range(x1[i] + offset, x2[i] + offset):
        for k in range(y1[i] + offset, y2[i] + offset):
            plane[j][k] = 1

total = sum(sum(row) for row in plane)
print(total)