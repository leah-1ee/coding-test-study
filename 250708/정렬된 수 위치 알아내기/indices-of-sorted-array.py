n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 클래스 생성
class Num:
    def __init__(self, num, index):
        self.num = num
        self.index = index
        self.rank = 0

# 객체 생성
nums = [Num(n, i) for i, n in enumerate(sequence)]

# 값 기준 정렬 
nums.sort(key = lambda x: x.num)

# 순위 부여
for i in range(1, n+1):
    nums[i-1].rank = i

# 인덱스 기준 정렬 
nums.sort(key = lambda x: x.index)

# 출력 
for n in nums:
    print(n.rank, end = ' ')