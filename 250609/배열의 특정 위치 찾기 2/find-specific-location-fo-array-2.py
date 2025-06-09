lst = list(map(int, input().split()))

# 짝수/홀수 리스트 
even_lst = lst[1::2]
odd_lst = lst[::2]

# 짝수 번째 합 / 홀수 번째 합 계산 
even_sum = sum(even_lst)
odd_sum = sum(odd_lst)

# 합이 더 큰 쪽에서 작은 쪽 빼기 
if even_sum > odd_sum:
    print(even_sum - odd_sum)
else:
    print(odd_sum - even_sum)