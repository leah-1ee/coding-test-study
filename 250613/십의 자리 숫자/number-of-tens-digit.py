lst = list(map(int, input().split()))
count = [0]*9

# 십의 자리 숫자 카운트 
for n in lst:
    if n == 0:
        break

    elif n>=10:
        num = (n//10)-1
        count[num] += 1



for i, j in enumerate(count, start=1):
    print(f"{i} - {j}")