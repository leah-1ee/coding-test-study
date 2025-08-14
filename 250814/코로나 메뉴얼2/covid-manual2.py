a_cou=0
b_cou=0
c_cou=0
d_cou=0

for i in range(3):
    s, t = input().split()
    t=int(t)
    
    if s=='Y':
        if t>=37:
            a_cou += 1
        else:
            c_cou += 1

    else:
        if t>=37:
            b_cou += 1
        else:
            d_cou += 1

print(f"{a_cou} {b_cou} {c_cou} {d_cou}", end=" ")

if a_cou>=2:
    print("E")



