class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_divisibles_by_k(k):
            m = n//k
            return k*m*(m+1)//2
        return sum_divisibles_by_k(3)+sum_divisibles_by_k(5)+sum_divisibles_by_k(7)-sum_divisibles_by_k(15)-sum_divisibles_by_k(21)-sum_divisibles_by_k(35)+sum_divisibles_by_k(105)
