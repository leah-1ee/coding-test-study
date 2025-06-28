s = input()

for elem in s:
    if elem.isdigit():
        print(elem, end = '')
    elif elem.isalpha():
        print(elem.lower(), end = '')

