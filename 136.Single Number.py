class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        summation = 0
        for i in nums:
            summation = summation ^ i
        return summation
        
