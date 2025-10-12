class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num < 2:
            return True

        left, right = 0, num // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
