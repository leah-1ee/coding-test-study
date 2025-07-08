a, b, c, d = map(int, input().split())

# Please write your code here.
past = a*60 + b
future = c*60 + d

print(future - past)