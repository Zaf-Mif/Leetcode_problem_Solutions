class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinks = rem = numBottles 
        
        while rem >= numExchange:
            div = rem // numExchange
            drinks += div
            rem = (rem % numExchange) + div
        
        return drinks
