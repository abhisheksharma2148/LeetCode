class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y= int(a,2), int(b,2)
        while y!=0:
            partial = x ^ y
            carry = (x & y) << 1
            x, y = partial, carry

        return(f'{x:b}')
