s = list(input())
second = s[1]

for i in range(len(s)):
    if s[i] == second:
        s[i] = s[0]

print(''.join(s))