class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = 1
        sq_rt = int(math.sqrt(num))
        if num==1:
            return False
        for i in range(2,sq_rt+1):

            if num%i ==0:
                
                other_divisor = num//i if num//i!=i else 0
                divisors+= i + other_divisor

        
        return divisors == num
