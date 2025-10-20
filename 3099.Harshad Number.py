class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits, n = 0,x
        while x>0:
            sum_of_digits += x%10
            x//=10
        if n%sum_of_digits ==0:
            return sum_of_digits
        else:
            return -1
