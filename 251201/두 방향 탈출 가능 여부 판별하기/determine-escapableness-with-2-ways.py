import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 방문 표기 
visited = [[False] * m for _ in range(n)]

# 아래 / 오른쪽 방향 이동 가능 
dr = [1, 0]
dc = [0, 1]

# dfs 탐색 
def dfs(r,c):
    # 종료 조건 : 우하단 도달
    if r == n-1 and c == m-1:
        return True
    
    # 아래 / 오른쪽 이동 
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 안 & 뱀 없음 & 방문x -> 다음 방문 좌표 
        if 0 <= nr < n and 0 <= nc < m and \
        grid[nr][nc] == 1 and visited[nr][nc] == False:
            visited[nr][nc] = True 
            if dfs(nr, nc):
                return True 
    # 이동 불가능하면 
    return False 

# dfs 재귀 순회 
if dfs(0, 0):
    print(1)
else:
    print(0)