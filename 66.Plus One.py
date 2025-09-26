class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= int("".join(map(str,digits)))
        s +=1
        b = [int(num) for num in str(s)]
        return b
        
