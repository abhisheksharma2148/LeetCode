class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNoZeroInteger(x,y):
            while x>0:
                d=x%10
                if d==0:
                    return False
                x //=10
            while y>0:
                d=y%10
                if d==0:
                    return False
                y//=10
            return True
        s = []
        for i in range(1,n//2+1):
            if isNoZeroInteger(i,n-i):
                s.append(i)
                s.append(n-i)
                return s
