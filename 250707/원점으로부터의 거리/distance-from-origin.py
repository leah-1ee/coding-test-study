n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(1, n+1)]

# Please write your code here.
class Dot:
    def __init__(self, num, point):
        self.num = num
        self.point = point

dots = [Dot(n, point) for n, point in points]

dots.sort(key = lambda x: (abs(x.point[0]) + abs(x.point[1])))

for d in dots:
    print(d.num)