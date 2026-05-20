def solution(m, n, puddles):
    puddle_set = set()
    for r, c in puddles:
        puddle_set.add((c-1, r-1))
        
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if (i, 0) in puddle_set:
            break
        dp[i][0] = 1
        
    for j in range(m):
        if (0, j) in puddle_set:
            break
        dp[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in puddle_set:
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[n-1][m-1] % 1000000007