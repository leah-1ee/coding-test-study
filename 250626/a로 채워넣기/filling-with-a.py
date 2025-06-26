s = input()
s = list(s)

s[1] = 'a'
s[-2] = 'a'


print(''.join(s))