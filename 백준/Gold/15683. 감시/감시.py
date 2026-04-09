import sys
sys.setrecursionlimit(2000)

def area_check(N, M, grid):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if grid[i][j] == 0:
        cnt += 1
  return cnt


def mark(r, c, d, grid, N, M):
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]
  marked = []
  
  nr, nc = r + dr[d], c + dc[d]
  while(0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 6):
    grid[nr][nc] += 1
    marked.append((nr, nc))
    nr, nc = nr + dr[d], nc + dc[d]

  return (marked, grid)


def unmark(marked, grid):
  for mr, mc in marked:
    grid[mr][mc] -= 1

  return grid


def CCTV(N, M, grid, CCTV_list, idx):
  global min_area 
  if idx == len(CCTV_list):
    area = area_check(N, M, grid)
    min_area = min(min_area, area)
    return
 
  r, c, k = CCTV_list[idx]
  if k == 1:
    for d in range(4):
      marked, grid = mark(r, c, d, grid, N, M)

      CCTV(N, M, grid, CCTV_list, idx+1)

      grid = unmark(marked, grid)
  
  elif k == 2:
    for d in range(2):
      marked1, grid = mark(r, c, d, grid, N, M)
      marked2, grid = mark(r, c, d+2, grid, N, M)

      CCTV(N, M, grid, CCTV_list, idx+1)

      grid = unmark(marked1, grid)
      grid = unmark(marked2, grid)
      
  elif k == 3:
    for d in range(4):
      marked1, grid = mark(r, c, d, grid, N, M)
      marked2, grid = mark(r, c, (d+1)%4, grid, N, M)

      CCTV(N, M, grid, CCTV_list, idx+1)

      grid = unmark(marked1, grid)
      grid = unmark(marked2, grid)


  elif k == 4:
    for d in range(4):
      marked1, grid = mark(r, c, d, grid, N, M)
      marked2, grid = mark(r, c, (d+1)%4, grid, N, M)
      marked3, grid = mark(r, c, (d+2)%4, grid, N, M)

      CCTV(N, M, grid, CCTV_list, idx+1)

      grid = unmark(marked1, grid)
      grid = unmark(marked2, grid)
      grid = unmark(marked3, grid)
      
  else:
    marked1, grid = mark(r, c, 0, grid, N, M)
    marked2, grid = mark(r, c, 1, grid, N, M)
    marked3, grid = mark(r, c, 2, grid, N, M)
    marked4, grid = mark(r, c, 3, grid, N, M)

    CCTV(N, M, grid, CCTV_list, idx+1)

    grid = unmark(marked1, grid)
    grid = unmark(marked2, grid)
    grid = unmark(marked3, grid)
    grid = unmark(marked4, grid)


N, M = map(int, input().split())

grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

CCTV_list = []
for i in range(N):
  for j in range(M):
    k = grid[i][j]
    if k != 0 and k != 6:
      CCTV_list.append((i, j, k))
      grid[i][j] = -100


min_area = sys.maxsize

CCTV(N, M, grid, CCTV_list, 0)
print(min_area)
