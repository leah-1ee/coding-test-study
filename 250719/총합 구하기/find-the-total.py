n1, n2 = map(int, input().split())
s = 0

for i in range(n1, n2+1):
    if (i%6==0 and i%8!=0):
        s += i
print(s)