


def func(arr: list)-> bool:
    prev = arr[0]
    for val in arr:
        if prev > val:
            return False
        prev = val
    return True

print(func([1,2,2,3,3,5]))
print(func([1,2,2,3,3,2]))
print(func([1,2,1,3,4]))


