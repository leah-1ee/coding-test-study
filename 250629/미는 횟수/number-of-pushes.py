A = input()
B = input()
flag = False

for i in range(len(A)):
    rotated = A[i:] + A[:i]
    
    if rotated == B:
        print(i)
        flag = True
        break

if flag == False:
    print(-1)