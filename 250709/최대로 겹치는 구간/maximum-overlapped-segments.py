n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 선분 저장할 배열
lines = [0] * 100

# 겹치는 구간 계산
for start, end in segments:
    for i in range(start, end):
        lines[i] += 1

# 가장 많이 겹치는 곳 출력 
print(max(lines))