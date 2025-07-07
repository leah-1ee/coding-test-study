n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

stds = [Student(h, w, n) for h, w, n in students]

stds.sort(key = lambda x: (x.height, -x.weight))

for s in stds:
    print(f"{s.height} {s.weight} {s.num}")