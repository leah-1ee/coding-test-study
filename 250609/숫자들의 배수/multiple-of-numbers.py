n = int(input())
arr = []
count, i = 0, 1

# 배수 계산해 더하기 
while True:
    num = n * i
    i += 1
    arr.append(num)
    
    # 5의 배수 체크 
    if num % 5 == 0:
        count += 1
        if count == 2:
            break
    


print(' '.join(map(str, arr)))