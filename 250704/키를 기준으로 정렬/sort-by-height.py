n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

infos = [Info(n, h, w) for n, h, w in zip(name, height, weight)]

infos.sort(key = lambda x: x.height)

for person in infos:
    print(f"{person.name} {person.height} {person.weight}")