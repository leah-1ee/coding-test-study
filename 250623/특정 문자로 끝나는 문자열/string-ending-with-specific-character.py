arr = [input() for _ in range(10)]
alp = input()

matches = [word for word in arr if word[-1] == alp]

if matches:
    for word in matches:
        print(word)

else:
    print("None")
