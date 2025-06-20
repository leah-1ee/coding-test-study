# 입력받기
n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

# 정답 배열
lst = []

# 값이 같으면 0 아니면 1
for i in range(n):
    row = []
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            row.append(0)
        else:
            row.append(1)
    lst.append(row)

for row in lst:
    print(*row)
