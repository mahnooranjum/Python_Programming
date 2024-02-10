
n_rows = 10
n_columns = 10

for i in range(n_rows):
    start = "A"
    for j in range(i):
        print(start, end="")
        start = chr(ord(start) + 1)
    
    print("")