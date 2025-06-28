s = input()

for elem in s:
    if elem >= 'A' and elem <= 'Z':
        print(elem.lower(), end = '')
    else:
        print(elem.upper(), end = '')