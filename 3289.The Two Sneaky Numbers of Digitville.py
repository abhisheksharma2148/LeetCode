class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        seen =set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                l.append(i)
        return l
