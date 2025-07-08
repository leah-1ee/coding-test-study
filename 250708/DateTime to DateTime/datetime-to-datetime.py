a, b, c = map(int, input().split())

# Please write your code here.
minite = (a-11) * 24 * 60 + (b-11) * 60 + (c-11)
if minite < 0:
    minite = -1
print(minite)