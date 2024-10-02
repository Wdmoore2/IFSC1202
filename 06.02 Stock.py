def percentchange(today, yesterday):
    """Calculate the percent change between today's and yesterday's stock price."""
    return ((today - yesterday) / yesterday) * 100

# Open and read the stock prices from the file
with open('06.02 Stock.txt', 'r') as file:
    prices = file.readlines()

# Print headings
print(f"{'Day':<10}{'Stock Price':<10}{'Percent Change':<10}")

# Process the first stock price
if prices:
    yesterday_price = float(prices[0].strip())
    print(f"{1:<10}{yesterday_price:<10.2f}{'N/A':<10}")

    # Process the remaining stock prices
    for i in range(1, len(prices)):
        today_price = float(prices[i].strip())
        change = percentchange(today_price, yesterday_price)
        
        # Print today's stock price and the percent change
        print(f"{i + 1:<10}{today_price:<10.2f}{change:<10.2f}")
        
        # Update yesterday's price
        yesterday_price = today_price
