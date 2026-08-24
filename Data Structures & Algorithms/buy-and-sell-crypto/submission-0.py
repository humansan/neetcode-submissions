class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cur_min = prices[0]
        max_profit = 0

        # keep a tracking minimum (represents local minimum seen so far)
        # iterate through the prices
        # max profit at that price is that price - local minimum seen so far
        # max profit is the max profit seen across all iterations

        for price in prices:
            cur_profit = price - cur_min
            max_profit = max(max_profit, cur_profit)
            
            cur_min = min(cur_min, price)
        
        return max_profit