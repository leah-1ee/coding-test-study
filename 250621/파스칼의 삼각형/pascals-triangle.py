n = int(input())

# 1로 채운 배열 
arr = [[1]*(i+1) for i in range(n)]

# i는 2부터, j는 1부터 시작, j는 i-1까지 반복 (삼각형 모양) 
for i in range(2, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


for row in arr:
    print(*row)