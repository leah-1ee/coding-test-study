from curses import BUTTON1_RELEASED
from collections import deque 
def tomato(N, M, grid, queue):
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]
  least_day = 0
  while (queue):
    r, c, day = queue.popleft()
    least_day = max(least_day, day)
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
        grid[nr][nc] = 1
        queue.append((nr, nc, day+1)) 

  for i in range(N):
    for j in range(M):
      if grid[i][j] == 0:
        return -1

  return least_day

  
        
    

M, N = map(int, input().split())

grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

queue = deque()
visited = [[False] * M for _ in range(N)]
for i in range(N):
  for j in range(M):
    if grid[i][j] == 1:
      queue.append((i, j, 0))


print(tomato(N, M, grid, queue))