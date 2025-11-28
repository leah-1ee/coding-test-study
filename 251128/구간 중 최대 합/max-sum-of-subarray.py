n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_total = 0
for i in range(n-k+1):
    total = sum(arr[i:i+k])
    max_total = max(max_total, total)

print(max_total)