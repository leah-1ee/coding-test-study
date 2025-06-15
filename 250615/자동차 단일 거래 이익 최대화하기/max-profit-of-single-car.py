n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
# 최저가 매입 
min_val = min(price)
i = price.index(min_val)

# 매입 이후 가격만 남기기 
price = price[i:]

# 이익 계산
money = max(price) - min_val

# 이익 없으면 0 출력 
if money <=0:
    print("0")
else:
    print(money)