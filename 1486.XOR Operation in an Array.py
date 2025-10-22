class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        count = 0
        xor = 0
        while count<n:
            xor ^= (start +(2*count))
            count +=1
        return xor
