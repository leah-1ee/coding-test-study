arr = [] # 250 미만의 수를 저장할 리스트 

lst = list(map(int, input().split())) # 10개 수 입력받기 

# 250 이상의 수 나오면 루프 종료, 아니면 arr에 추가 
for num in lst:
    if num >= 250:
        break
    else:
        arr.append(num)

# 합, 평균 계산 
total = sum(arr)
avr = total / len(arr)


print(f"{total} {avr:.1f}")
