class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter,maxlen = 0,0
        for i in nums:
            if i==1:
                counter+=1
                maxlen = max(maxlen,counter)
            else:
                counter =0
        return maxlen
