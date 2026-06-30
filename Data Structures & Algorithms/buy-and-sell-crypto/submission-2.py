class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        r = l + 1
        n = len(prices)

        while r < n:
            if prices[l] < prices[r]:
                res = max(prices[r] - prices[l], res)
            else:
                l = r
            r += 1

        return res
        # [5, 1, 5, 6, 7, 1, 10] 