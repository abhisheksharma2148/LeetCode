class Solution:
    def countDigits(self, num: int) -> int:
        original,counter  = num,0
        
        while num>0:
            if original%(num%10) ==0:
                counter+=1
            num//=10
        return counter
