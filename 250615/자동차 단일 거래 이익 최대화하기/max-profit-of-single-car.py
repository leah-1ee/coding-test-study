n = int(input())
prices = list(map(int, input().split()))

# Please write your code here.
min_price = float('inf')
profit = 0

# 최소값 갱신하면서 최대이익 찾기 
for price in prices:
    min_price = min(price, min_price)
    profit = max(price-min_price, profit)

print(profit)
