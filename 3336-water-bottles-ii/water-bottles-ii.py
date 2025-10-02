class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = rem = numBottles
        while rem >= numExchange:
            drink += 1
            rem -= numExchange - 1
            numExchange += 1
        return drink