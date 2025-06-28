n = int(input())
total = 0

for i in range(n):
    num = int(input())
    total += num

total = str(total)
total = total[1:] + total[0]
print(total)