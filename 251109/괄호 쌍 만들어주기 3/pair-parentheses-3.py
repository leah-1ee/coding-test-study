A = input()

# Please write your code here.
num = 0

# ( 체크 
for i in range(len(A)):
    if A[i] == '(':
        # ) 나오면 num + 1 
        for j in range(i, len(A)):
            if A[j] == ')':
                num += 1

print(num)