A = input()
total = 0

for elem in A:
    if elem.isdigit():
        total += int(elem)

print(total)