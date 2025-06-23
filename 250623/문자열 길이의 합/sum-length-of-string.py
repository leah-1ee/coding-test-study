n = int(input())

arr = [input() for _ in range(n)]
num = 0
cnt = 0

for i in range(n):
    num += len(arr[i])
    if arr[i][0] == 'a':
        cnt += 1

print(f"{num} {cnt}")