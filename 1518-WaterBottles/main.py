class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            tmp = numBottles // numExchange
            count += tmp
            numBottles = tmp + numBottles % numExchange

        return count


numBottles = 15
numExchange = 4

sol = Solution()
result = sol.numWaterBottles(numBottles, numExchange)
print(result)
