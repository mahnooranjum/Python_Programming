def func(arr:list)->int:
    a = 0
    b = 0
    for i in arr:
        if i == 1:
            a=a+1
            if a>b:
                b=a
        else:
            a=0

    return b


print(func([1,1,2,3,4,1,1,1,1,2,3,1,1]))