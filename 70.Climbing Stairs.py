class Solution:
    def climbStairs(self, n: int) -> int:
        prev_0 ,prev_1=1,1
        curr = 0
        for x in (range(1,n+1)):
            if x<=1:
                curr =1            
            else:
                curr = prev_0 +prev_1
                prev_0= prev_1
                prev_1 =curr
            
                
        return curr
            
