# Search the array for the lowest value from left to right
# Then search the array for the highest value from left to right

# So 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0] # Our lowest value will be on the first day, then
        for price in prices: # For each day...
            if price < lowest: # If the current day's price is lower than the first day or previous day
                lowest = price # Set the new lowest to the current one
            res = max(res, price - lowest) # Our profit will be the higher of itself or the current day minus the lowest day
        return res # Return profit

