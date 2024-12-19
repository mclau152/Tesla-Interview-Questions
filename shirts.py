def max_profit(prices):
    # Initialize variables
    min_price = float('inf')  # Start with a very high minimum price
    max_profit = 0            # Start with zero profit
    
    # Traverse through the list of prices
    for price in prices:
        # Update the minimum price (buying price)
        if price < min_price:
            min_price = price
        
        # Calculate potential profit if sold on this day
        profit = price - min_price
        
        # Update the maximum profit if this profit is higher
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]  # Prices of shirts over several days
result = max_profit(prices)
print("Maximum profit:", result)
