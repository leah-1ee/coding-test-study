lst = list(map(int, input().split()))
arr = []

# 짝수면 2로 나눠서 추가, 홀수면 3을 더해서 추가, 0이면 종료 
for n in lst:
    if n != 0:
        if n % 2 == 0:
            arr.append(n//2)
        else:
            arr.append(n+3)
    
    else:
        break

print(' '.join(map(str, arr)))