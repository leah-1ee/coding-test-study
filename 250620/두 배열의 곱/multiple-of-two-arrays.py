# 두 배열 입력받기, 공백 줄 처리
arr1 = [list(map(int, input().split())) for _ in range(3)]
line = input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

# 같은 인덱스끼리 곱하기
lst = [[a*b for a,b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]

#출력
for rows in lst:
    print(*rows)