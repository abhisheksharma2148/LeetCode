class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = int(str(n)[::-1])
        sign = 1
        sum =0
        while n>0:
            sum += sign*(n%10)
            sign *=-1
            n//=10
        return sum
