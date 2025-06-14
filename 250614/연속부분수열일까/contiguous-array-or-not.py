n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 슬라이싱해서 B가 부분수열인지 확인
found = any(A[i:i+n2] == B for i in range(n1-n2+1))

if found == True:
    print("Yes")
else:
    print("No")
