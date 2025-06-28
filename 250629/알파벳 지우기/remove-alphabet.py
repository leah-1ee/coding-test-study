a = input()
b = input()

a = ''.join(x for x in a if x.isdigit())
b = ''.join(x for x in b if x.isdigit())

print(int(a) + int(b))