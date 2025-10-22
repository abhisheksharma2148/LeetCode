class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mins, maxs = nums[0] ,nums[0]
        for i in nums:
            mins = min(mins,i)
            maxs = max(maxs,i)

            gcd =1

        for i in range(1,mins+1):
            if mins%i==0 and maxs%i==0:
                gcd =i
        return gcd
