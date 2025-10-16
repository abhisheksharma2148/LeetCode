class Solution:
    def maxProduct(self, n: int) -> int:
        max1, max2=-1,-1
        while n>0:
            d = n%10
            if d >= max1:
                max2 = max1
                max1 =d
            elif d>= max2:
                max2 = d
            n //=10
        return max1*max2
