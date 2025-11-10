R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# 이동 성공 경우의 수
# W <-> B
# 최소 i,j + 1
# 2개만 밟아야 함

# 경우의 수 세기 
cnt = 0
# 초기 위치 
r, c = 0, 0

# 첫 번째 점프 
for nr in range(1, R-1):
    for nc in range(1, C-1):
        # 색 다른 곳으로 점프 
        if grid[r][c] != grid[nr][nc]:
            # 두 번째 점프 
            for nnr in range(nr+1, R-1):
                for nnc in range(nc+1, C-1):
                    # 색 다른 곳으로 점프 
                    if grid[nr][nc] != grid[nnr][nnc]:
                        cnt += 1

print(cnt)
