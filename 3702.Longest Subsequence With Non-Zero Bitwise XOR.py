class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for i in nums:
            total_xor ^= i
        if total_xor != 0:
         return len(nums)
        else:
            if any(i!=0 for i in nums):
                return len(nums)-1
            else:
                return 0
