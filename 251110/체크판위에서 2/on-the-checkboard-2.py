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
for nr in range(1, R-2):
    for nc in range(1, C-2):
        # 색 다른 곳으로 점프 
        if grid[r][c] != grid[nr][nc]:
            # 두 번째 점프 
            for nnr in range(nr+1, R-1):
                for nnc in range(nc+1, C-1):
                    # 색 다른 곳으로 점프 
                    if grid[nr][nc] != grid[nnr][nnc]:
                        # 세 번째 점프는 없어야 함 
                        for nnnr in range(nnr+1, R):
                            for nnnc in range(nnc+1, C):
                                # 도착 지점 도달 시 조건 3 만족 
                                if grid[nnr][nnc] != grid[nnnr][nnnc] and\
                                nnnr == R-1 and nnnc == C-1:
                                    cnt += 1

print(cnt)
