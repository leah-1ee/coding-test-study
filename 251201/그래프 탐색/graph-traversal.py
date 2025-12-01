import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def dfs(cur_v):
    visited[cur_v] = True
    cnt = 1
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            cnt += dfs(next_v)

    return cnt 

total = dfs(1)
print(total-1)