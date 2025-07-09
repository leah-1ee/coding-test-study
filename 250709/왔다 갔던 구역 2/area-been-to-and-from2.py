n = int(input())
x = []
direction = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    direction.append(di)

# Please write your code here.
area = [0] * 1000
start = 500 # 중심 설정, 음수 인덱스 방지 

# 이동 계산
for i in range(n):
    if direction[i] == 'L': # 왼쪽 이동 
        # L 이동은 도착 포함, 출발 제외
        # R 이동은 출발 포함, 도착 제외 (진행 방향 반대이므로)
        
        # 도착지 포함, 출발지 제외 위해 range 시작, 끝에 -1씩 
        for j in range(start - 1, start - x[i] - 1, -1): # 움직인 구역 체크 
            area[j] += 1
        start -= x[i] # start 지점 설정 

    elif direction[i] == 'R': # 오른쪽 이동 
        for j in range(start, start + x[i]): # 출발지 포함, 도착지 제외 
            area[j] += 1
        start += x[i]

# 겹치는 구역 세기 
cnt = 0

for i in range(len(area)):
    if area[i] >= 2:
        cnt += 1

print(cnt)