class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                print("i, j", i, j)
                if prices[i] > prices[j]:
                    continue
                
                res = max(res, prices[j] - prices[i])

        return res
        # [5, 1, 5, 6, 7, 1, 10]