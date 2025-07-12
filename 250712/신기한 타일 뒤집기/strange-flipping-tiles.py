n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
directions = []
for num, direction in commands:
    x.append(int(num))
    directions.append(direction)

# Please write your code here.
# 모든 명령 거리 합으로 배열 초기화
max_move = sum(x)
tiles = ['G'] * (max_move * 2 + 1)
start = max_move    # 음수인덱스 방지 시작 지점 설정 

# 타일 칠하기 
# 시작 포함, 끝 불포함, 방향 상관없이
for i in range(n):
    if directions[i] == 'L':
        for j in range(start, start - x[i], -1):
            tiles[j] = 'W'
        start = start - x[i] + 1
    if directions[i] == 'R':
        for j in range(start, start + x[i]):
            tiles[j] = 'B'
        start = start + x[i] - 1

# 카운트 변수 초기화 
cnt_white, cnt_black = 0, 0

# 흰, 검 타일 수 세기 
for t in tiles:
    if t == 'W':
        cnt_white += 1
    elif t == 'B':
        cnt_black += 1

print(f"{cnt_white} {cnt_black}")