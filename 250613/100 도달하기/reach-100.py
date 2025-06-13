n = int(input())

arr = [1, n]

# 전항과 전전항을 더해서 배열에 추가, 100 넘으면 종료
while True:
    num = arr[-1] + arr[-2]
    arr.append(num)
    if num > 100:
        break

print(' '.join(map(str, arr)))