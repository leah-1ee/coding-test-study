arr = []
lst = list(map(int, input().split()))

for num in lst:
    if num == 0:
        break
    else:
        arr.append(num)

total = sum(arr)
avr = round(total / len(arr), 1)

print(total, end = ' ')
print(avr)