def func(arr:list)->list:


    for i in range(0, len(arr)):
        j = -1
        if arr[i] == 0 and j==-1:
            j = i
            break
    
    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            arr[i] = 0
            j= j+1

            
    return arr


print(func([0,1,2,0,3,4,0,0,0,5,6,7,8,0]))