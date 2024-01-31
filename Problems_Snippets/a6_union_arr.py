import sys
def func(arr1:list, arr2:list)->list:
    arr1.sort()
    arr2.sort()

    arr = []

    i = 0
    j = 0

    while j < len(arr2) and i < len(arr1):
        if arr1[i] <= arr2[j]:
            if len(arr) == 0:
                arr.append(arr1[i])
            elif arr[-1] != arr1[i]:
                arr.append(arr1[i])
            i = i+1
        else:
            if len(arr) == 0:
                arr.append(arr2[j])
            elif arr[-1] != arr2[j]:
                arr.append(arr2[j])
            j = j+1

    while i < len(arr1):
        if arr[-1] != arr1[i] or len(arr) == 0:
            arr.append(arr1[i])
        i = i+1
    while j < len(arr2):
        if arr[-1] != arr2[j] or len(arr) == 0:
            arr.append(arr2[j])
        j = j + 1


    return arr

print(func([1,2,3,4,5,6,7,8,9],[3,5,2,4,5,3,3,2,1,4,5,6,7,8,9,0]))
print(func([3,5,2,4,5,3,3,2,1,4,5,6,7,8,9,0], [8,29,34,6,7,8,9,0,3,5]))