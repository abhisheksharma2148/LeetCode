class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_selfDividingNumber(x):
            original = x
            while x > 0:
                d= x%10
                if d==0 or original%d!=0:
                    return False
                x//=10
            return True
        sdn =[]
        for num in range(left, right+1):
            if is_selfDividingNumber(num):
                sdn.append(num)
        return sdn
        
