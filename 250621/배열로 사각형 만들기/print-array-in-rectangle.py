arr = [[1]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i>=1 and j>=1:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]


for row in arr:
    print(*row)