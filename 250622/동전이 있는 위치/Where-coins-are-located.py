n, m = map(int, input().split())

arr = [[0]*n for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

for row in arr:
    print(*row)