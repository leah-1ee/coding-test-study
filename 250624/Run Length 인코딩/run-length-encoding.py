A = input()

# Please write your code here.
arr = []
cnt = 1

for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cnt += 1

    else:
        arr.append(A[i-1])
        arr.append(str(cnt))
        cnt = 1

arr.append(A[-1])
arr.append(str(cnt))

answer = ''.join(arr)
print(len(answer))
print(answer)