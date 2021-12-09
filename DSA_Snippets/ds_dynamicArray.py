
import ctypes 


class DynamicArray(object):
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if (not 0 <= k < self.n):
            return IndexError('Index is out of bounds')
        return self.A[k]
    
    def append(self, value):
        if self.n == self.capacity:
            self._resize()
        self.A[self.n] = value
        self.n += 1
        
    def _resize(self):
        self.capacity *= 2
        referencer = self.make_array(self.capacity)
        for k in range(self.n):
            referencer[k] = self.A[k]
            # references 
        self.A = referencer 
    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
            
        
myArr = DynamicArray()
myArr.append(1)
myArr.append(2)
myArr.append(3)
print(len(myArr))   
print(myArr[2])  