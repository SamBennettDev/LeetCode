class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        i = 0

        while (i < len(prices)):
            lowest = prices[i]

            while(i < len(prices) - 1 and prices[i + 1] > prices[i]):
                i += 1

            total += prices[i] - lowest
            i += 1

        return total