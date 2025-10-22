class Solution:
    def countEven(self, num: int) -> int:
        def isdigitsumeven(x):
            d=0
            while x>0:
                d+= x%10
                x//=10
            return d%2==0
        
        counter=0
        
        for i in range(2,num+1):
            if isdigitsumeven(i):
                counter+=1
        return counter
        
