class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            x = str(i)
            maxval = max(x)
            total += int(maxval*len(x))
        return total
