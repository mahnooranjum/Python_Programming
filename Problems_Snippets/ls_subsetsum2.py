


class Solution:
    
    def call(self):
        arr = [1,2,2]
        n = len(arr)
        arr.sort()
        ans = []
        def func(idx, ds):
            print(ds)
            
            for i in range(idx, n):
                if i>idx and arr[i] == arr[i-1]:
                    continue
                
                ds.append(arr[i])
                func(i+1, ds)
                ds.pop()
            
            
        func(0,[])
        print(ans)
        


sol = Solution()
sol.call()