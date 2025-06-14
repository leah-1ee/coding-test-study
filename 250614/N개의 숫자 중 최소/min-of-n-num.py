n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = min(a)
cnt = a.count(min_val)

print(f"{min_val} {cnt}")