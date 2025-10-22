class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n,1000):
            p =1
            x = i
            while x>0:
                d = x%10
                p *=d
                x//=10
            if p%t==0:
                return i
