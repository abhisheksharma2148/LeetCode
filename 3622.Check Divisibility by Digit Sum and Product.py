class Solution:
    def checkDivisibility(self, n: int) -> bool:

        s, p =0,1
        x =n
        while n>0:
            s += n%10
            p *= n%10
            n//=10
        
        return x%(s+p)==0
