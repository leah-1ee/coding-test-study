n, m = map(int, input().split())

arr = [[0]*n for _ in range(n)]
num = 1

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = num
    num += 1

for row in arr:
    print(*row)