class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num>0:
            num = num -1 if num&1 else num>>1
            counter+=1
        return counter
        
