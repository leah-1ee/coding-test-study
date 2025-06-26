s1, s2 = list(input().split())
s2 = list(s2)

s2[0:2] = s1[0:2]

print(''.join(s2))