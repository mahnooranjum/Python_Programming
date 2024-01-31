

def func(arr:list, d: int)->list:
    d = d%len(arr)
    temp = arr[0:d]
    for i in range(0, len(arr)-1):
        if (i+d)<len(arr):
            arr[i] = arr[i+d]

    arr[-d:] = temp
    return arr


def func1(arr:list, d: int)->list:
    d = d%len(arr)
    temp = arr[0:d]
    arr[0:len(arr)-d]=arr[d:]
    arr[-d:] = temp
    return arr


def func2(arr:list, d: int)->list:
    d = d%len(arr)
    arr[0:d] = reversed(arr[0:d])
    arr[d:] = reversed(arr[d:])
    arr = reversed(arr)
    return list(arr)


print(func2([1,2,3,4,5,6,7,8,9],3))