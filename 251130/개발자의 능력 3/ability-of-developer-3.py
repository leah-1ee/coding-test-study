abilities = list(map(int, input().split()))

# Please write your code here.

n = len(abilities)
total = sum(abilities)
min_diff = float('inf')

for i in range(n-2):
    for j in range(1, n-1):
        for k in range(2, n):
            group1 = abilities[i] + abilities[j] + abilities[k]
            group2 = total - group1
            diff = abs(group1 - group2)
            min_diff = min(min_diff, diff)

print(min_diff)