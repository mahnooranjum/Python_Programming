
# %%
import sys
def func(arr: list) -> list:
    l = -sys.maxsize - 1
    sl = -1

    for val in arr:
        if val > l:
            sl = l
            l = val

    return [l, sl]

print(func([1,2,2,3,4,5,7,7,7]))


# %%
