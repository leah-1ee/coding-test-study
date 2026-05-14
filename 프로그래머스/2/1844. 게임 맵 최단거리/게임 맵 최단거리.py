from collections import deque

def bfs(n, m, maps):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    r, c = 0, 0
    
    queue.append((r, c, 1))
    visited[r][c] = True 
    
    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == m-1:
            return dist
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                queue.append((nr, nc, dist+1))
                visited[nr][nc] = True
    return -1
    

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    return bfs(n, m, maps)
    