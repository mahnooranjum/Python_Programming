

class Solution:
    
    def call(self):
        arr = [1,2,3]
        n = len(arr)
        
        def func(idx, ds):
            if idx==(n):
                print(ds)
                return
                
            for i in range(idx, n):
                               
                ds.append(arr[i])
                temp = arr[idx]
                arr[idx] = arr[i]
                arr[i] = temp
                
                func(idx+1, ds)
                
                temp = arr[idx]
                arr[idx] = arr[i]
                arr[i] = temp
                ds.pop()
                
           
        func(0, [])
        


sol = Solution()
sol.call()