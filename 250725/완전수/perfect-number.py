start, end = map(int, input().split())
s=0
count = 0

for i in range(start, end+1):
    for j in range(1, i):
        if(i%j==0):
            s += j
    if (s==i):
        count+= 1
    s=0

print(count)
    
