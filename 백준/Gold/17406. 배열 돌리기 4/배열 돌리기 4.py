import sys
sys.setrecursionlimit(2000)

def array_val(N, M, grid):
  min_row = sys.maxsize 
  
  for i in range(N):
    row = 0
    for j in range(M):
      row += grid[i][j]
    min_row = min(min_row, row)
  return min_row


def rotate(i, j, s, grid, n):
  start_r = i - s
  start_c = j - s
  end_r = i + s
  end_c = j + s
  
  if n == 0:
    # 시계방향 동남서북
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
  else: # 반시계 남동북서
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]


  while(True):
    d = 0
    prev_val = grid[start_r][start_c]
  
    r = start_r + dr[d]
    c = start_c + dc[d]
  
    # 한 번 돌기 (가장 외곽)
    while(True):
      if r == start_r and c == start_c:
        grid[r][c] = prev_val
        break

      temp = grid[r][c]
      grid[r][c] = prev_val
      prev_val = temp 
    
      nr, nc = r + dr[d], c + dc[d]
      if not(start_r <= nr <= end_r and start_c <= nc <= end_c):
        d = (d+1) % 4
        nr, nc = r + dr[d], c + dc[d]
      r, c = nr, nc

    start_r = start_r + 1
    start_c = start_c + 1
    end_r = end_r - 1
    end_c = end_c - 1
    if start_r == end_r and start_c == end_c:
      return grid
  


def dfs(N, M, K, grid, rotation, cnt, visited):
  global answer
  if cnt == K:

    min_array = array_val(N, M, grid)
    answer = min(answer, min_array)
    return 

  for k in range(K):
    if not visited[k]:
      i, j, s = rotation[k]
      visited[k] = True
      grid = rotate(i, j, s, grid, 0)

      dfs(N, M, K, grid, rotation, cnt+1, visited)
      
      grid = rotate(i, j, s, grid, 1)
      visited[k] = False
    

N, M, K = map(int, input().split())

grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

rotation = []
for _ in range(K):
  i, j, s = map(int, input().split())
  rotation.append((i-1, j-1, s))

answer = sys.maxsize
visited = [False] * K
dfs(N, M, K, grid, rotation, 0, visited)
print(answer)