N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_diff = float('inf')

for i in range(N-1):
    for j in range(1, N):
        new_arr = arr[:i] + arr[i+1:j] + arr[j+1:]
        arr_sum = sum(new_arr)
        diff = abs(arr_sum - S)
        min_diff = min(min_diff, diff)

print(min_diff)