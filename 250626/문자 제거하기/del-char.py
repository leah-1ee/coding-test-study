s = list(input())

while len(s)>1:
    n = int(input())
    if n < len(s):
        s.pop(n)
    else:
        s.pop(-1)

    print(''.join(s))