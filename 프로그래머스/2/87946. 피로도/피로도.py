max_visit = 0

def dfs(dungeons, visited, N, k, visit):
    global max_visit
    max_visit = max(max_visit, visit)
        
    for i in range(N):
        if visited[i]:
            continue
        
        least, use = dungeons[i]
        
        if k >= least:
            visited[i] = True
            dfs(dungeons, visited, N, k - use, visit + 1)
            visited[i] = False
        

def solution(k, dungeons):
    global max_visit
    max_visit = 0
    
    N = len(dungeons)
    visited = [False] * N
    
    dfs(dungeons, visited, N, k, 0)
    return max_visit