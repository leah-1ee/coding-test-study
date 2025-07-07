n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

persons = [Info(n, h, w) for n, h, w in zip(name, height, weight)]

persons.sort(key = lambda x: x.name)

print("name")
for p in persons:
    print(f"{p.name} {p.height} {p.weight}")

persons.sort(key = lambda x: -x.height)

print("\nheight")
for p in persons:
    print(f"{p.name} {p.height} {p.weight}")