class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = ""
        sign = "-" if num<0 else ""
        x = abs(num)
        if num ==0:
            return "0"
        while x>0:
            base7 += str(x%7)
            x//=7
        return sign+base7[::-1]
