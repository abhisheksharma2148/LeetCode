class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            if (i >= 10 and i < 100) or (i>=1000 and i <10000) or (i==100000):
                counter +=1
        return counter
#class Solution:
#    def findNumbers(self, nums: List[int]) -> int:
#        def is_even_no_of_digits(x):
#            digits = 0
#            if x < 10:
#                return False
#            while x:
#                x //=10
#                digits+=1
#            return digits%2==0
#        counter =0
#        for i in nums:
#            if is_even_no_of_digits(i):
#                counter+=1
#        return counter
