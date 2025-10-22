class Solution:
    def averageValue(self, nums: List[int]) -> int:
        counter, sum = 0,0
        for i in nums:
            if i%6==0:
                counter +=1
                sum+=i
        return sum//counter if counter!=0 else 0
