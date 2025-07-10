n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dirc = []
for num, direction in commands:
    x.append(int(num))
    dirc.append(direction)

# Please write your code here.
# Tile 정보 저장: b/w 몇 번 거쳤는지, 마지막 색 정보 저장
class Tile:
    def __init__(self):
        self.black = 0
        self.white = 0
        self.color = 'N'

# Tile 배열, 음수 인덱스 방지 위한 시작 지점 설정 
tiles = [Tile() for _ in range(20)]
start = 10

# 타일 칠하기, 시작 포함 끝 포함하지 않음 (방향상관없이) 
# 끝부분 포함하지 않으므로 start 갱신 시 뒤로 한 칸

for i in range(n):
    if dirc[i] == 'L':
        for j in range(start, start - x[i], -1):
            tiles[j].color = 'W'
            tiles[j].white += 1
        start = start - x[i] + 1

    elif dirc[i] == 'R':
        for j in range(start, start + x[i]):
            tiles[j].color = 'B'
            tiles[j].black += 1
        start = start + x[i] - 1


# 흰, 검, 회색 타일 수 세기
# 색 초기값인 경우 패스
# 흰, 검 2회 이상 칠해진 경우 회색
# 마지막으로 칠해진 색 세기
cnt_black, cnt_white, cnt_gray = 0, 0, 0
for t in tiles:
    if t.color == 'N':
        continue
    elif t.black >= 2 and t.white >= 2:
        cnt_gray += 1
    elif t.color == 'B':
        cnt_black += 1
    elif t.color == 'W':
        cnt_white += 1
    
    
# 출력
print(f"{cnt_white} {cnt_black} {cnt_gray}")