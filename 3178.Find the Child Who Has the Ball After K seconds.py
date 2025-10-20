class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        pointer , time , direction = 0,1, 1
        while time<=k:
            pointer += direction
            if pointer == 0 or pointer == (n-1):
                direction *= -1
            time +=1
            
        return pointer
