
# Patterns 

n_rows = 10
n_columns = 10

# block
for _ in range(n_rows):
    print("*" * n_columns)


# upper triangle
for k in range(n_rows):
    print("*" * k)


# lower triangle
for k in range(n_rows):
    print("*" * (n_columns-k))


# upper triangle
for k in range(n_rows):
    print(" " * (n_columns-k),end="")
    print("*" * (1+((k-1)*2)))


for k in range(n_rows):
    print(" " * (k),end="")
    print("*" * (n_columns+((k-1)*(-2))+1))


for k in range(n_rows*2):
    if (k<(n_rows)):
        print(" " * (n_columns-k),end="")
        print("*" * (1+((k-1)*2)))
        val = (1+((k-1)*2))
    else:
        k = k%n_rows
        print(" " * (k),end="")
        print("*" * (val+((k-1)*(-2))))
        


for k in range(n_rows):
    if (k<=(n_rows/2)):
        print("*"*k)
    else:
        print("*"*(n_rows-k))