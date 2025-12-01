import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    if r == n-1 and c == m-1:
        return True
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m and \
        grid[nr][nc] == 1 and visited[nr][nc] == False:
            visited[nr][nc] = True 
            print(f"{nr} {nc}")
            if dfs(nr, nc):
                return True 
    return False 

if grid[0][0] == 1 and dfs(0, 0):
    print(1)
else:
    print(0)