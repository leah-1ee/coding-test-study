lst = list(map(int, input().split()))

# 짝수 번째 입력 배열 
even_lst = lst[1::2]

# 3의 배수 번째 입력 배열 
three_lst = lst[2::3]

# 합/평균 계산 
even_sum = sum(even_lst)
avr = round(sum(three_lst) / len(three_lst), 1)

print(even_sum, end=' ')
print(avr)