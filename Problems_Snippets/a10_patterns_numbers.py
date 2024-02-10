
n_rows = 10
n_columns = 10

for i in range(n_rows):
    start = 1 if i%2==0 else 0
    for j in range(i):
        print(start, end="")
        start = 1-start
    print("")



n_rows = 4
n_columns = 8

for i in range(n_rows):
    for j in range(i+1):
        print(j, end="")

    for _ in range(((n_rows-i)-1)*2, 0, -1):
        print(" ", end="")

    for j in range(i,-1,-1):
        print(j, end="")

    print("")

