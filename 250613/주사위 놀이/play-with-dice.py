lst = list(map(int, input().split()))

count = [0] * 6

for n in lst:
    count[n-1] += 1

for i, j in enumerate(count, start = 1):
    print(f"{i} - {j}")