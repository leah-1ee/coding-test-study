a, b = input().split()
total = str(int(a) + int(b))
cnt = 0

for i in total:
    if i == '1':
        cnt += 1

print(cnt)