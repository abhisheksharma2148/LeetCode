class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        counter =0
        for i in stones:
            if i in jewel:
                counter+=1
        return counter
