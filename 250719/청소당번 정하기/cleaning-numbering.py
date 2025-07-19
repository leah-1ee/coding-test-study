n = int(input())

clas = 0
out = 0
bath = 0

for i in range(1, n+1, 1):
    if (i%12==0):
        bath += 1
    elif (i%3==0):
        out += 1
    elif (i%2==0):
        clas += 1
print(f"{clas} {out} {bath}")
