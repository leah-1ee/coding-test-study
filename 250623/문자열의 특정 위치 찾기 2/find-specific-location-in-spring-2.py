arr = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()
cnt = 0

for i in range(5):
    for j in range(2,4):
        if arr[i][j] == a:
            print(arr[i])
            cnt += 1
            continue

print(cnt)