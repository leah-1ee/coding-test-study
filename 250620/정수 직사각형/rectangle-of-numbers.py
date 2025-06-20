n, m = map(int, input().split())  # n: 행, m: 열
arr = []  # 결과를 담을 배열
num = 1   # 채워넣을 숫자

for i in range(n):
    row = []
    for j in range(m):
        row.append(num)
        num += 1
    arr.append(row)

for row in arr:
    print(*row)
