n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class Student:
    def __init__(self, name, kr, eng, math):
        self.name = name
        self.kr = kr
        self.eng = eng
        self.math = math

students = [Student(n, k, e, m) for n, k, e, m \
            in zip(name, korean, english, math)]

students.sort(key = lambda x: (-x.kr, -x.eng, -x.math))

for s in students:
    print(f"{s.name} {s.kr} {s.eng} {s.math}")