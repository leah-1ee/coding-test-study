n, m = map(int, input().split())

arr = [[0]*n for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    num = i * j
    arr[i-1][j-1] = num

for row in arr:
    print(*row)