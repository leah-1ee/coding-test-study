n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

# 객체 배열 만들기 
persons = [Person(n, a, r) for n, a, r in zip(name, street_address, region)]

# 이름이 가장 뒤인 사람 추출 
target = max(persons, key = lambda x: x.name)

print(f"name {target.name}")
print(f"addr {target.address}")
print(f"city {target.region}")