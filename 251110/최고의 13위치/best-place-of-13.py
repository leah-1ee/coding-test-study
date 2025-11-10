n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1 * 3 격자 
# 합 최대

# 최대 합 저장할 변수 
max_sum = 0

# 완전 탐색 시작 
for i in range(n):
    for j in range(n-2):
        # 1 * 3 격자 합 
        new_sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        # 최댓값 업데이트 
        max_sum = max(max_sum, new_sum)

print(max_sum)