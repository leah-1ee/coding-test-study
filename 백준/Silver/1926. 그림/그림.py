"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

from collections import deque

def bfs(grid, start_r, start_c, N, M, visited):
  
  queue = deque() 

  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]

  visited[start_r][start_c] = True
  queue.append((start_r, start_c))
  size = 1

  while(queue):
    r, c = queue.popleft()
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i] 
      if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == 1:
        size += 1
        visited[nr][nc] = True
        queue.append((nr, nc))

  return size 

N, M = map(int, input().split())
grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

visited = [[False] * M for _ in range(N)]
cnt = 0
biggest = 0

for i in range(N):
  for j in range(M):
    if grid[i][j] == 1 and not visited[i][j]:
      size = bfs(grid, i, j, N, M, visited)
      cnt += 1
      biggest = max(biggest, size)

print(cnt)
print(biggest)