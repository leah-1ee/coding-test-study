cnt3 =0 
cnt5=0

for i in range(10):
    n=int(input())

    if (n%3==0 and n%5==0):
        cnt3 += 1
        cnt5 += 1

    elif (n%5==0):
        cnt5 += 1

    elif (n%3==0):
        cnt3 += 1
        

print(f"{cnt3} {cnt5} ")
