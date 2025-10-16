class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        no_of_bottles_drank, emptied=numBottles, numBottles
        while emptied>= numExchange:
            new_full = emptied//numExchange
            no_of_bottles_drank += new_full
            emptied = new_full + (emptied%numExchange)
            
        return no_of_bottles_drank

#return numBottles + (numBottles-1)//(numExchange-1)
