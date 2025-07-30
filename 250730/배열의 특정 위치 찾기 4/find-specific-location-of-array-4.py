num=list(map(int, input().split()))
result=[]

for i in num:
    if i==0:
        break
    elif (i%2==0):
        result.append(i)
    else:
        continue

print(len(result), sum(result))