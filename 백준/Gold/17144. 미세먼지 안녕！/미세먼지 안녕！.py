def dust_count(N, M, grid):
  cnt = 0
  for i in range(N):
      for j in range(M):
          if grid[i][j] > 0:
              cnt += grid[i][j]
  return cnt

def simulate(N, M, grid, cleaner, T):
  # 상, 하, 좌, 우
  dr_spread = [-1, 1, 0, 0]
  dc_spread = [0, 0, -1, 1]

  for _ in range(T):
      # 1. 미세먼지 확산
      new_grid = [row[:] for row in grid]
      for i in range(N):
          for j in range(M):
              if grid[i][j] > 0:
                  val = grid[i][j]
                  spread_amount = val // 5
                  spread_cnt = 0

                  for d in range(4):
                      nr, nc = i + dr_spread[d], j + dc_spread[d]
                      # 공기청정기가 아닌 빈 칸으로만 확산
                      if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != -1:
                          new_grid[nr][nc] += spread_amount
                          spread_cnt += 1

                  # 원래 칸에서는 확산된 총량만큼 한 번에 빼기
                  new_grid[i][j] -= (spread_amount * spread_cnt)

      grid = new_grid

      # 2. 공기청정기 가동
      r1, c1 = cleaner[0]
      r2, c2 = cleaner[1]
      grid = clean(r1, c1, 0, grid, N, M)
      grid = clean(r2, c2, 1, grid, N, M)

  return dust_count(N, M, grid)

def clean(start_r, start_c, n, grid, N, M):
  # n == 0: 위쪽 청정기 (반시계) / 우, 상, 좌, 하
  if n == 0:
      dr = [0, -1, 0, 1]
      dc = [1, 0, -1, 0]
      min_r, max_r = 0, start_r
  # n == 1: 아래쪽 청정기 (시계) / 우, 하, 좌, 상
  else:
      dr = [0, 1, 0, -1]
      dc = [1, 0, -1, 0]
      min_r, max_r = start_r, N - 1

  d = 0
  r, c = start_r + dr[d], start_c + dc[d]
  prev_value = 0  # 공기청정기에서 갓 나온 맑은 공기 (0)

  while True:
      # 공기청정기 위치로 다시 돌아오면 종료 (먼지 소멸)
      if grid[r][c] == -1:
          break

      # 먼지를 밀어내는 핵심 로직 (Swap X, Temp O)
      temp = grid[r][c]
      grid[r][c] = prev_value
      prev_value = temp

      nr, nc = r + dr[d], c + dc[d]

      # 지정된 위/아래 구역을 벗어나면 방향을 꺾음
      if not (min_r <= nr <= max_r and 0 <= nc < M):
          d = (d + 1) % 4
          nr, nc = r + dr[d], c + dc[d]

      r, c = nr, nc

  return grid

# --- 입력 및 실행 ---
N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cleaner = []
for i in range(N):
  if grid[i][0] == -1:
      cleaner.append((i, 0))

print(simulate(N, M, grid, cleaner, T))