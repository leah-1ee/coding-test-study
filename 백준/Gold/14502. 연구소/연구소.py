from collections import deque 
import sys
sys.setrecursionlimit(2000)

def bfs(N, M, grid):
  queue = deque()
  for i in range(N):
    for j in range(M):
      if grid[i][j]== 2:
        queue.append((i, j))
   
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]
  copy_grid = [row[:] for row in grid]
  
  while(queue):
    r, c = queue.popleft() 

    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if 0 <= nr < N and 0 <= nc < M and copy_grid[nr][nc] == 0:
        copy_grid[nr][nc] = 2
        queue.append((nr, nc))

  cnt = 0
  for i in range(N):
    for j in range(M):
      if copy_grid[i][j]== 0:
        cnt += 1
        
  return cnt


def dfs(wall, N, M, grid):
  global max_cnt
  
  if wall == 0:
    cnt = bfs(N, M, grid)
    max_cnt = max(max_cnt, cnt)
    return
  
  for i in range(N):
    for j in range(M):
      if grid[i][j]== 0:
        grid[i][j] = 1
        dfs(wall-1, N, M, grid)
        grid[i][j] = 0


N, M = map(int, input().split())
grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

max_cnt = 0
dfs(3, N, M, grid)
print(max_cnt)