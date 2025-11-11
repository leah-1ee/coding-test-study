a_str = input()
# a_str -> 10진수 정수 
decimal = int(a_str, 2)

max_num = 0
n = len(a_str)

# 2진수의 한 자리를 바꾸는 것 = 2의 i제곱을 더하거나 뺴는 것 
for i in range(n):
    # 2의 제곱: n-1 n-2 ... 0
    # i       : 0   1   ... n-1
    # -> n-1-i 로 계산 
    power_of_2 = 2 ** (n - 1 - i)

    # 1 -> 0 이면 빼기 
    if a_str[i] == '1':
        current = decimal - power_of_2
    # 0 -> 1 이면 더하기 
    else:
        current = decimal + power_of_2
    # 최댓값 업데이트 
    max_num = max(max_num, current)

print(max_num)