n = int(input())
arr = []
num = 1

for i in range(n):
    row = []
    elem = num
    for j in range(n):
        row.append(elem)
        elem += n
        
    arr.append(row)
    num += 1

for row in arr:
    print(*row)