a, b = map(int, input().split())

arr = [a, b]

# 전항과 전전항 더해서 1의자리 추출, 리스트에 추가 
for i in range(8):
    n = (arr[-1]+arr[-2]) % 10
    arr.append(n)

print(' '.join(map(str, arr)))
