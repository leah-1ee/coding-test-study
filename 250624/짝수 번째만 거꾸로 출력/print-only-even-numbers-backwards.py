A = input()

arr = [A[i] for i in range(len(A)) if i % 2 == 1]

arr.reverse()

print(''.join(arr))