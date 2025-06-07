arr = []
lst = list(input().split())

for num in lst:
    if num != '0':
        arr.append(num)
    else:
        break

reverse = ' '.join(arr[::-1])
print(reverse)