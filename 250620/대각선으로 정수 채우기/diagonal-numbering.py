n, m = map(int, input().split())

# Please write your code here.


arr = [[0]*m for _ in range(n)]
num = 1

# 대각선을 따라 채우기
for s in range(n+m-1): # 대각선 수 n+m-1
    for i in range(n):
        j = s-i
        if 0 <= j < m:
            arr[i][j] = num
            num += 1

for row in arr:
    print(*row)