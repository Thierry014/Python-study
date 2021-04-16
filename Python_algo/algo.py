 # ! Calculate Sum
 ## 1. loop 

def sumToK(k):
    res = 0 
    for i in range(k+1):
        res += i
    
    return res

print(sumToK(5))

## 2. formular 

def sumToL(l):
    return ((l*(l+1))/2)


 #TODO: use %timeit function() to test run time in jupyter notebook  

