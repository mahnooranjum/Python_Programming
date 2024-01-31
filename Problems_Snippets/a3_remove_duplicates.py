
# sorted
def func(arr:list)->list:
    cur = 0
    for i in range(1, len(arr)):
        if (arr[i] != arr[cur]):
            arr[cur+1] = arr[i]
            cur = cur+1
        
    return arr[0:cur+1]

print(func([1,1,1,2,2,3,3,3,4]))

