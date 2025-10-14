class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,candidate = 0, 0
        for x in nums:
            if count ==0:
                candidate = x
                count = 1
            elif candidate ==x:
                count +=1
            else:
                count -=1
        return candidate
