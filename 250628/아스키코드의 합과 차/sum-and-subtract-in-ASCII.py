a, b = input().split()

print(ord(a) + ord(b), end=' ')
print(ord(a) - ord(b) if ord(a) > ord(b) else ord(b) - ord(a))
