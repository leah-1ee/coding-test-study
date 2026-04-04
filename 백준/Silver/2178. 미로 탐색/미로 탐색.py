"""
4 6
101111
101010
101011
111011
"""

from collections import deque 

def bfs(grid, start_r, start_c, N, M):
  visited = [[False] * M for _ in range(N)]
  queue = deque()

  visited[start_r][start_c] = True 
  queue.append((start_r, start_c, 1))

  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]


  while(queue):
    r, c, dist = queue.popleft()
    if r == N-1 and c == M-1:
      return dist 
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == 1:
        visited[nr][nc] = True 
        queue.append((nr, nc, dist+1))
  

N, M = map(int, input().split())
grid = []
for _ in range(N):
  row = list(map(int, input()))
  grid.append(row)

cnt = bfs(grid, 0, 0, N, M)
print(cnt)