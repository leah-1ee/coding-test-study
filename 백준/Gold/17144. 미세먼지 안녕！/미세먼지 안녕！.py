"""
7 8 3
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
"""

def count_grid(N, M, grid):
  cnt = 0
  
  for i in range(N):
    for j in range(M):
      if grid[i][j] > 0:
        cnt += grid[i][j]
        
  return cnt

def clean(start_r, start_c, n, N, M, grid):
  if n == 0:
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    min_r, max_r = 0, start_r

  else:
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    min_r, max_r = start_r, N-1


  d = 0
  r, c = start_r + dr[d], start_c + dc[d]
  prev_val = 0
  
  while(True):
    if grid[r][c] == -1:
      return grid

    temp = grid[r][c]
    grid[r][c] = prev_val
    prev_val = temp

    nr, nc = r + dr[d], c + dc[d]
    if not (min_r <= nr <= max_r and 0 <= nc < M):
      d = (d+1) % 4
      nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc
  

def simulation(N, M, T, grid, cleaner):
  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]
  
  for _ in range(T):
    new_grid = [row[:] for row in grid]
    
    for r in range(N):
      for c in range(M):
        
        if new_grid[r][c] > 0:
          spread_cnt = 0
          val = grid[r][c] // 5
          
          for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in cleaner:
              spread_cnt += 1
              new_grid[nr][nc] += val
              
          new_grid[r][c] -= (val * spread_cnt)

    grid = new_grid

    r1, c1 = cleaner[0]
    r2, c2 = cleaner[1]
    grid = clean(r1, c1, 0, N, M, grid)
    grid = clean(r2, c2, 1, N, M, grid)

  return count_grid(N, M, grid)
            

N, M, T = map(int, input().split())

grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

cleaner = []
for i in range(N):
  if grid[i][0] == -1:
    cleaner.append((i, 0))

print(simulation(N, M, T, grid, cleaner))