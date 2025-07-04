n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Std:
    def __init__(self, height, weight, n):
        self.height = height
        self.weight = weight
        self.n = n

stds = [Std(h, w, n) for h, w, n in students]

stds.sort(key = lambda x: (-x.height, -x.weight, x.n))

for s in stds:
    print(f"{s.height} {s.weight} {s.n}")