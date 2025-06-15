n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

print(max([x for x in nums if nums.count(x)==1], default=-1)) 