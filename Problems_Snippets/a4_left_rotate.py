

def func(arr:list)->list:
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp
    return arr


print(func([1,2,3,4,5,6,7,8,9]))