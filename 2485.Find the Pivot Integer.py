class Solution:
    def pivotInteger(self, n: int) -> int:
        target = n*(n+1)//2
        s = math.isqrt(target)
        return s if s*s == target else -1
