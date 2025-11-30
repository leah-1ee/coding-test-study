N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.

a1, b1, c1 = a1+N, b1+N, c1+N
a2, b2, c2 = a2+N, b2+N, c2+N
a1_scope = [i%N for i in range(a1-2, a1+3)]
a2_scope = [i%N for i in range(a2-2, a2+3)]
b1_scope = [i%N for i in range(b1-2, b1+3)]
b2_scope = [i%N for i in range(b2-2, b2+3)]
c1_scope = [i%N for i in range(c1-2, c1+3)]
c2_scope = [i%N for i in range(c2-2, c2+3)]

a_set = set(a1_scope + a2_scope)
b_set = set(b1_scope + b2_scope)
c_set = set(c1_scope + c2_scope)

a_diff = len(a1_scope + a2_scope) - len(a_set)
b_diff = len(b1_scope + b2_scope) - len(b_set)
c_diff = len(c1_scope + c2_scope) - len(c_set)

diff = a_diff * b_diff * c_diff

if N >= 5:
    test = 250 - diff 
    
else:
    test = (N ** 3) - diff


print(test)