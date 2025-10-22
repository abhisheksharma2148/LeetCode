class Solution:
    def sumBase(self, n: int, k: int) -> int:
        base_k = 0
        while n>0:
            base_k += n%k
            n //=k
        return base_k
