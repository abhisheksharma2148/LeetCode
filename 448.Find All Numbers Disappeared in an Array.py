class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length_of_nums = len(nums)
        missing_nums = []
        nums_set = set(nums)
        for i in range(1,length_of_nums+1):
            if i not in nums_set:
                missing_nums.append(i)
        return missing_nums
