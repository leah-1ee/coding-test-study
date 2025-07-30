lst=list(map(int, input().split()))

hol=lst[1::2]
jak=lst[::2]
re=0

if sum(hol)>sum(jak):
    re = sum(hol) - sum(jak)
else:
    re = sum(jak) - sum(hol)

print(re)