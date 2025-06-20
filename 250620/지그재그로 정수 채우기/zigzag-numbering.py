n, m = map(int, input().split())

# Please write your code here.
arr = []

for i in range(n):
    row = []
    for j in range(m):
        if j%2 == 0:
            row.append(j*n + i)
        else:
            row.append((j+1)*n -i-1)
    arr.append(row)

for row in arr:
    print(*row)
