class Solution:
    def tribonacci(self, n: int) -> int:
        prev_1, prev_2,prev_3 =0,1,1
        tribonacci_number = 0
        if n <=0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            for i in range(3,n+1):
                tribonacci_number = prev_1 + prev_2 + prev_3
                prev_1 = prev_2
                prev_2 =prev_3
                prev_3 = tribonacci_number
            return tribonacci_number
            
