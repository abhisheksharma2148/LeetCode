class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits , prod_of_digits = 0,1
        while n >0:
            t = n%10
            sum_of_digits += t
            prod_of_digits *=t
            n //=10
        return prod_of_digits - sum_of_digits
        
