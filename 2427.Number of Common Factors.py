class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        i =1
        minofboth = min(a,b)
        while i <= minofboth:
            if a%i ==0 and b%i==0:
                counter+=1
            i +=1
        return counter
