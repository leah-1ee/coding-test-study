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
        for j in range(start, start - x[i], -1): # 움직인 구역 체크 
            area[j] += 1
        start -= x[i] # start 지점 설정 

    elif direction[i] == 'R': # 오른쪽 이동 
        for j in range(start, start + x[i]):
            area[j] += 1
        start += x[i]

# 겹치는 구역 세기 
cnt = 0

for i in range(len(area)):
    if area[i] >= 2:
        cnt += 1

print(cnt)