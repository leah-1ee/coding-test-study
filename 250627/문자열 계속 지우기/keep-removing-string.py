A = input()
B = input()

# Please write your code here.
while B in A:
    idx = A.find(B)
    A = A[:idx] + A[idx+len(B):]

print(''.join(A))