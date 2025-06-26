s, n = input().split()

s = list(s)
n = int(n)

for i in range(n):
    qus = list(input().split())

    if qus[0] == '1':
        qus = list(map(int, qus))
        temp = s[qus[1]-1]
        s[qus[1]-1] = s[qus[2]-1]
        s[qus[2]-1] = temp

    elif qus[0] == '2':
        for i in range(len(s)):
            if s[i] == qus[1]:
                s[i] = qus[2]
                
    print(''.join(s))
