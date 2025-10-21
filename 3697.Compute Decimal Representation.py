class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        base10 = []
        unit = 0
        while n >0:
            if n%10 !=0:
                base10.append((n%10)*(10**unit))
            n//=10
            unit+=1
        return base10[::-1]
