import sys
def func(a:list, b:list)->list:
    a.sort()
    b.sort()

    arr = []

    i = 0
    j = 0

    while j < len(b) and i < len(a):
        if a[i] > b[j]:
            j = j+1
        elif a[i] < b[j]:
            i = i+1
        else:
            if len(arr) == 0:
                arr.append(a[i])
                i = i+1
                j = j+1
            elif arr[-1] != a[i]:
                arr.append(a[i])
                i = i+1
                j = j+1
    
    # while i < len(a):
    #     if arr[-1] != a[i] or len(arr) == 0:
    #         arr.append(a[i])
    #     i = i+1

    # while j < len(b):
    #     if arr[-1] != b[j] or len(arr) == 0:
    #         arr.append(b[j])
    #     j = j+1


    return arr

print(func([1,2,3,4,5,6,7,8,9],[3,5,2,4,5,3,3,2,1,4,5,6,7,8,9,0]))
print(func([3,5,2,4,5,3,3,2,1,4,5,6,7,8,9,0], [8,29,34,6,7,8,9,0,3,5]))