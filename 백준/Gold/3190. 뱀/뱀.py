from collections import deque

def game(N, grid, x_list, c_list):
  
  time = 1
  r, c = 0, 0
  grid[0][0] = 2
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]
  d = 1
  snake = deque()
  snake.append((0,0))
  idx = 0
  
  while(True):   
    
    nr, nc = r + dr[d], c + dc[d]   
    
    if 0 <= nr < N and 0 <= nc < N:
      if grid[nr][nc] == 2:
        return time
      elif grid[nr][nc] == 0:
        del_r, del_c = snake.popleft()
        grid[del_r][del_c] = 0

      r, c = nr, nc
      grid[r][c] = 2
      snake.append((r, c))

    else:
      return time

    if idx < len(x_list) and time == x_list[idx]:
      if c_list[idx] == 'D':
        d = (d + 1) % 4
      else: # L
        d = (d + 3) % 4
      idx += 1
  
    time += 1


N = int(input())
K = int(input())

grid = [[0] * N for _ in range(N)]

for _ in range(K):
  i, j = map(int, input().split())
  grid[i-1][j-1] = 1

L = int(input())
x_list = []
c_list = []
for _ in range(L):
  x, c = input().split()
  x_list.append(int(x))
  c_list.append(c)

print(game(N, grid, x_list, c_list))