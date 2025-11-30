N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# 최대 사탕, 현재 사탕 합, 위치 별 사탕 수 저장할 배열 
max_candy = 0
current_candy = 0
arr = [0] * (max(pos) + 1)

# 배열에 사탕 수 기록 
for i in range(len(pos)):
    arr[pos[i]] += candy[i]

# 윈도우 크기
window = 2 * K + 1

# 초기 윈도우 사탕 수 구하기 
limit = min(len(arr), window)
for i in range(limit):
    current_candy += arr[i]
max_candy = current_candy

# 윈도우를 한 칸씩 이동하면서 사탕 수 계산 
for i in range(window, len(arr)):
    current_candy += arr[i]
    current_candy -= arr[i-window]
    max_candy = max(max_candy, current_candy) 

print(max_candy)