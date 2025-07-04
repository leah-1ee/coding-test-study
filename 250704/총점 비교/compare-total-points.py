n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Std:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2 
        self.s3 = s3

students = [Std(n, s1, s2, s3) for n, s1, s2, s3 in zip(name, score1, score2, score3)]

students.sort(key = lambda x: x.s1 + x.s2 + x.s3)

for s in students:
    print(f"{s.name} {s.s1} {s.s2} {s.s3}")