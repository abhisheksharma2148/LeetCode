class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def sum_of_square_of_digits(n):
            sums = 0
            while n > 0:
                d = n%10
                sums += d*d
                n //= 10
            return sums
        while n >1:
            if n not in seen:
                seen.add(n)
                n = sum_of_square_of_digits(n)
            else:
                return n==1  
        return n==1
