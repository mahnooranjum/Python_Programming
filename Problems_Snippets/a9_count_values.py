
from collections import defaultdict
def func(arr:list)->int:
    d = defaultdict(int)
    for i in arr:
        d[i] = d[i]+1
    return [i for i in d.keys() if d[i] in [1,2]]



def func(arr:list)->int:
    
    once = arr[0]
    for i in arr[1:]:
        once = once ^ i
    return once

        
    
# print(func([1,1,2,3,4,1,1,2,2,2,1,1,2,3,1,1,6,6,9]))
print(func([1,1,2,2,3,3,4,5,5,6,6]))