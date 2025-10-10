class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 -1
        sign = -1 if x<0 else 1
        x =abs(x)
        rev =0
        while x >0:
            rev*=10
            rev+= x%10
            
            x//=10
        rev *=sign
        if rev < int_min or rev>int_max:
            return 0
        else:
            return rev
