class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        left, right = 0, 1
        max_profit = 0
        maximum_achievable_profit = max(prices) - min(prices)
        while right<n:
            if max_profit == maximum_achievable_profit:
                break
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            right += 1
        return max_profit
