"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""

from collections import deque 
def bfs(grid, start_r, start_c, N, visited):
  queue = deque()
  queue.append((start_r, start_c))

  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]
  size = 1
  
  while(queue):
    r, c = queue.popleft()
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]

      if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == 1:
        size += 1
        visited[nr][nc] = True
        queue.append((nr, nc))

  return size 

N = int(input())
grid = []
for _ in range(N):
  row = list(map(int, input()))
  grid.append(row)

visited = [[False] * N for _ in range(N)]
size_list = []
cnt = 0

for i in range(N):
  for j in range(N):
    if grid[i][j] == 1 and not visited[i][j]:
      cnt += 1
      visited[i][j] = True 
      size = bfs(grid, i, j, N, visited)
      size_list.append(size)

print(cnt)
size_list = sorted(size_list)
for s in size_list:
  print(s)