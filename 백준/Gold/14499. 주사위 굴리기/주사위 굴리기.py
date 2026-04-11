def dice(top, bottom, left, right, front, back, d):
  if d == 0:
    top, bottom, left, right, front, back = right, left, top, bottom, front, back
  elif d == 1:
    top, bottom, left, right, front, back = left, right, bottom, top, front, back
  elif d == 2:
    top, bottom, left, right, front, back = front, back, left, right, bottom, top
  else:
    top, bottom, left, right, front, back = back, front, left, right, top, bottom
  
  return top, bottom, left, right, front, back

def simulation(grid, x, y, K, order, N, M):
  top, bottom, left, right, front, back = 0, 0, 0, 0, 0, 0
  r, c = x, y
  # 동서북남
  dr = [0, 0, -1, 1]
  dc = [1, -1, 0, 0]

  for d in order:
    #print(d)
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < N and 0 <= nc < M:
      top, bottom, left, right, front, back = dice(top, bottom, left, right, front, back, d)

      r, c = nr, nc 

      if grid[r][c] == 0:
        grid[r][c] = bottom 
      else:
        bottom = grid[r][c]  
        grid[r][c] = 0

      print(top)
  

# 입력
N, M, x, y, K = map(int, input().split())

grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

order = list(map(int, input().split()))
order = [a-1 for a in order]

simulation(grid, x, y, K, order, N, M)