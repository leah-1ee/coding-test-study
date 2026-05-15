cnt = 0
def dfs(N, depth, result, numbers, target):
    global cnt
    if depth == N:
        if result == target:
            cnt += 1
        return
    
    dfs(N, depth+1, result+numbers[depth], numbers, target)
    dfs(N, depth+1, result-numbers[depth], numbers, target)

def solution(numbers, target):
    
    N = len(numbers)
    dfs(N, 0, 0, numbers, target)
    return cnt