lst=list(map(int, input().split()))

n=[]

for i in lst:
    if i==0:
        break
    n.append(i)

print(n[-1]+n[-2]+n[-3])