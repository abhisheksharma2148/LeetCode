class Solution:
    def isUgly(self, n: int) -> bool:
        factors = [2,3,5]
        if n==0:
            return False
        for k in factors:
            while not n%k:        
                n //=k        
        return n==1
