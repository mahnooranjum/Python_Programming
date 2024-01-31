def func(arr:list, d: int)->list:
    arr.sort()
    i = 0
    while i < len(arr)-1:
        if (arr[i+1] - arr[i] != 1):
            return arr[i]+1
            break
        i = i+1
    return -1

def func1(arr:list, d: int)->list:
    summa = sum(arr)
    summa_orig = d*(d+1)/2
    return summa_orig - summa


from functools import reduce
def func2(arr:list, d: int)->list:
    xor1 = reduce(lambda x, y: x ^ y, arr)
    xor2 = reduce(lambda x, y: x ^ y, range(1, d+1))
    return xor1 ^ xor2

print(func2([1,2,4,5], 5))