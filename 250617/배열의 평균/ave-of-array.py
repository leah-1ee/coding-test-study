arr = [list(map(int, input().split())) for _ in range(2)]

# 행 평균
row_avr = [round(sum(row)/4, 1) for row in arr]
print(*row_avr)

# 열 평균
col_avr = [round(sum(col)/2, 1) for col in zip(*arr)]
print(*col_avr)

# 전체 평균
print(round(sum(row_avr)/2, 1))

# *: 리스트 요소 하나씩 꺼내서 함수에 전달
# zip: 같은 인덱스끼리 묶어줌 