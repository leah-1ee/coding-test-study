s = input()

idx = s.find('e')
s = s[:idx] + s[idx+1:]

print(s)