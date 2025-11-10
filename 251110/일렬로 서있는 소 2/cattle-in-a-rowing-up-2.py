n = int(input())
cow_height = list(map(int, input().split()))

# 조건 만족 수 
cnt = 0

# i < j < k 조건 충족시키는 3중 반복문 
for i in range(n):
    for j in range(i+1, n):
        # A_i <= A_j 인 경우에만 넘어감 
        if cow_height[i] <= cow_height[j]:
            for k in range(j+1, n):
                # A_j <= A_k 까지 만족하면 cnt + 1 
                if cow_height[j] <= cow_height[k]:
                    cnt += 1


print(cnt)
