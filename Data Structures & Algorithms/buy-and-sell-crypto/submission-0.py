class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,0
        res = 0
        menor = prices[0]

        while r < len(prices) - 1:
            r += 1

            if prices[r] > menor:
                res = max(res, prices[r] - menor)
            else:
                l = r
                menor = prices[r]

        return res