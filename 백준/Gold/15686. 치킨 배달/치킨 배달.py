import sys

def dist(N, M, grid, selected):
  city_dist = 0
  
  for r1 in range(N):
    for c1 in range(N):
      
      if grid[r1][c1] == 1:
        house_dist = sys.maxsize
        
        for r2, c2 in selected:
          d = abs(r1-r2) + abs(c1-c2)
          house_dist = min(house_dist, d)
          
        city_dist += house_dist 
        
  return city_dist

def dfs(N, M, grid, chicken, cnt, selected, idx):
  global min_d 
  if cnt == M:
    d = dist(N, M, grid, selected)
    min_d = min(min_d, d)
    return 

  for i in range(idx, len(chicken)):
    selected.append(chicken[i])
    dfs(N, M, grid, chicken, cnt+1, selected, i+1)
    selected.pop()



N, M = map(int, input().split())

grid = []
for _ in range(N):
  row = list(map(int, input().split()))
  grid.append(row)

chicken = []
for i in range(N):
  for j in range(N):
    if grid[i][j] == 2:
      chicken.append((i, j))

min_d = sys.maxsize
selected = []

dfs(N, M, grid, chicken, 0, selected, 0)
print(min_d)