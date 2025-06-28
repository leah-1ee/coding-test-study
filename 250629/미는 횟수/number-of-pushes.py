A = input()
B = input()
flag = False

for i in range(len(A)):
    A = A[i:] + A[:i]
    if A == B:
        print(i+1)
        flag = True
        break

if flag == False:
    print(-1)