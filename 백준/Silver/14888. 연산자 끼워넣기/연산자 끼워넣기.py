import sys
sys.setrecursionlimit(2000)

def dfs(N, result, depth, nums, add, sub, mul, div):
  global large, small
  if depth == N:
    large = max(large, result)
    small = min(small, result)
    return

  if add > 0:
    dfs(N, result + nums[depth], depth+1, nums, add-1, sub, mul, div)

  if sub > 0:
    dfs(N, result - nums[depth], depth+1, nums, add, sub-1, mul, div)

  if mul > 0:
    dfs(N, result * nums[depth], depth+1, nums, add, sub, mul-1, div)

  if div > 0:
    if result >= 0:
      dfs(N, result // nums[depth], depth+1, nums, add, sub, mul, div-1)
    else:
      dfs(N, -((-result) // nums[depth]), depth+1, nums, add, sub, mul, div-1)

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
large = -sys.maxsize
small = sys.maxsize

dfs(N, nums[0], 1, nums, add, sub, mul, div)


print(large)
print(small)