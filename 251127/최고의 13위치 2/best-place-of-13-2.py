n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 최종 합 변수 
max_sum = 0

# 첫 번째 격자 위치 
for i in range(n):
    for j in range(n-2):
        coin1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        # 두 번째 격자 위치 
        for k in range(n):
            for l in range(n-2):
                # 격자 중복 방지 
                if k == i and j-2 <= l <= j+2:
                    continue
                else:
                    coin2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                    max_sum = max(max_sum, coin1 + coin2)

print(max_sum)