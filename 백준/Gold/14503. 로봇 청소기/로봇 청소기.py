def clean(r, c, d, grid):
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]

  cnt = 0

  while(True):
    if grid[r][c] == 0:
      grid[r][c] = 2
      cnt += 1

    for _ in range(4):
      d = (d+3) % 4
      nr, nc = r + dr[d], c + dc[d]

      if grid[nr][nc] == 0:
        r, c = nr, nc
        break 
    else:
      nr, nc = r - dr[d], c - dc[d]
      if grid[nr][nc] == 1:
        return cnt
      else:
        r, c = nr, nc 


N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = []

for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

print(clean(r, c, d, grid))