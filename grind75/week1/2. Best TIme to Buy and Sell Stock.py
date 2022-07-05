# Problem description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = len(prices)-1
        
        minimum = prices[0]
        maximum = prices[len(prices)-1]
        
        while left < right:
            
            if prices[left] < minimum:
                minimum = prices[left]
            left += 1
            
            if prices[right] > maximum:
                maximum = prices[right]
            right -= 1
            
        if (maximum-minimum) > 0: 
            return maximum-minimum 
        else:
            return 0 