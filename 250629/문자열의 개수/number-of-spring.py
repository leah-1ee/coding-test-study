cnt = 0
arr = []

while True:
    s = input()

    if s == '0':
        break

    else:
        cnt += 1
        if cnt % 2 != 0:
            arr.append(s)

print(cnt)
for elem in arr:
    print(elem)