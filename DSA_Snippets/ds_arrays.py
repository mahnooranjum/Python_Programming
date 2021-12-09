

'''

    A to new pointers, B stays back to 1,2,3
'''
A = [1,2,3]
B = A 
A = [6,7,8]
print(A, B)


'''
    Pointer to new value, both change

'''
B = A 
A[2] = 6
print(A, B)
 