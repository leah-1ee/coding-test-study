import sys
sys.setrecursionlimit(100000)

def dfs(grid, r, N, visited):
  visited[r] = True 

  cnt = 1

  for k in range(N):
    if grid[r][k] == 1 and not visited[k]:
      cnt += dfs(grid, k, N, visited)

  return cnt

N = int(input())
visited = [False] * N
grid = [[0] * N for _ in range(N)]

line = int(input())
for _ in range(line):
  i, j = map(int, input().split())
  grid[i-1][j-1] = 1
  grid[j-1][i-1] = 1

num = dfs(grid, 0, N, visited)

print(num-1)