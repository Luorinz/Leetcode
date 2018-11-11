# easy

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n^2) solution
        # TLE
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i] 
        return max_profit
    
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n) solution
        # Use 2 vars to record min and max price
        max_profit = 0
        min_price = float('inf')
        for i in prices:
            # Compare the current profit to the max profit
            min_price = min(i, min_price)
            profit = i - min_price
            max_profit = max(profit, max_profit)
        return max_profit
            
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n) solution DP
        # Use [lowest price so far, max profit so far] to update each price
        if prices is None or len(prices) < 2:
            return 0
        dp = [prices[0], 0]
        for i in range(1, len(prices)):
            # if curr price is min, then update the lowest price
            if prices[i] < dp[i-1][0]:
                dp.append([prices[i], dp[i-1][1]])
            else:
                profit = prices[i] - dp[i-1][0]
                # if max profit, update
                if profit > dp[i-1][1]:
                    dp.append(dp[i-1][0], profit)
                else:
                    # if not max profit, nothing changes
                    dp.append(dp[i-1])
        return dp[-1][1]
    
    
    