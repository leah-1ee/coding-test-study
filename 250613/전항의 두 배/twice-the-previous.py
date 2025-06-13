lst = list(map(int, input().split()))

for i in range(8):
    n = lst[-1] + 2*lst[-2]
    lst.append(n)

print(' '.join(map(str, lst)))