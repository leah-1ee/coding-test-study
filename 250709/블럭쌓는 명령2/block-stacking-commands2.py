n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 블럭을 놓을 배열 
blocks = [0] * (n+1)

# 명령 구간에 블럭 쌓기 
for start, end in commands:
    for i in range(start, end+1):
        blocks[i] += 1

# 최대 블럭 수 출력 
print(max(blocks))
