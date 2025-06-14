n = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i, num in enumerate(lst):
    if num == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)
