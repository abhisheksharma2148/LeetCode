class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for i in nums:
            if i ==0:
                return 0
            else:
                prod*=i
        return -1 if prod <0 else 1
