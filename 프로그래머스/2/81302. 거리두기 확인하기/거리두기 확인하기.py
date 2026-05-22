from collections import deque

def bfs(grid, queue, visited):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    while (queue):
        r, c, dist = queue.popleft()
        if dist == 2:
            continue
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                visited[nr][nc] = True
                if grid[nr][nc] == 'X':
                    continue
                if grid[nr][nc] == 'P':
                    return False
                queue.append((nr, nc, dist+1))
                
    return True
    

def solution(places):
    answer = []
    
    
    for place in places:
        grid = []
        for p in place:
            grid.append(list(p))
            
        check = True
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    visited[i][j] = True
                    queue = deque()
                    queue.append((i, j, 0))
                    check = bfs(grid, queue, visited)
                    if not check:
                        answer.append(0)
                        break
            if not check:
                break
        else:  
            answer.append(1)
    
    return answer