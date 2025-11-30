N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
arr = [0] * (max(pos)+1)
max_candy = 0

for i in range(N):
    arr[pos[i]] = candy[i]

for c in range(K, len(arr)-K):
    total = 0
    for j in range(c-K, c+K+1):
        total += arr[j]
    max_candy = max(max_candy, total)

print(max_candy)