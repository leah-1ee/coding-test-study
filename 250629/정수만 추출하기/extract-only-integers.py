a, b = input().split()

for elem in a:
    if not elem.isdigit():
        idx = a.find(elem)
        a = a[:idx]
        break

for elem in b:
    if not elem.isdigit():
        idx = b.find(elem)
        b = b[:idx]
        break

print(int(a) + int(b))