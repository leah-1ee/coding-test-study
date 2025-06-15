lst = list(map(int, input().split()))

print(max([x for x in lst if x<500]), end=' ')
print(min([x for x in lst if x>500]))