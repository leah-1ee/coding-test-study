
for i in range(1, 20):
    for j in range(1, 20):
        print(f"{i} * {j} = {i*j}", end="")
        if (j%2==0 or j==19):
            print()
        else:
            print(" / ", end="")
    #print()