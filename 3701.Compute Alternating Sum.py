class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        summation, alternator = 0, -1
        for i in nums:
            alternator *= -1
            summation = summation + (alternator * i)    
        return summation
