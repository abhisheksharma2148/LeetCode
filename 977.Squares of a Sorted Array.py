class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right = 0, len(nums)-1
        res = [0]*len(nums)
        pos = len(nums)-1
        while right >= left:
            left_sq = nums[left]*nums[left]
            right_sq = nums[right]*nums[right]
            if left_sq < right_sq:
                res[pos] = nums[right]*nums[right]
                right -=1
            else:
                res[pos] = nums[left] * nums[left]
                left +=1
            pos -=1
        return res
