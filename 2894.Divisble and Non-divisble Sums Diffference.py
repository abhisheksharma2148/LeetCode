class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        quotient = n//m
        return (n *(n+1)//2) - (quotient * (quotient+1))*m
