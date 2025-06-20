n = int(input())
arr = []

# i: 행 인덱스, j: 열 인덱스
for i in range(n):
    row = [(j * n) + (i + 1) for j in range(n)]  # 한 줄에 바로 계산해서 넣기
    arr.append(row)

# 출력
for row in arr:
    print(*row)
