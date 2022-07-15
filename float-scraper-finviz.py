from time import time
from finvizfinance.quote import finvizfinance

# Prompt for ticker symbol (e.g. AAPL)
stock = input('Enter ticker symbol:')

# Set start time to measure the speed of the whole operation
start = time()

# Get float from shortsqueeze.com
try:
    stock_data = finvizfinance(stock)
    stock_fundament = stock_data.ticker_fundament()
    print('Shares Float: ' + stock_fundament['Shs Float'])
    print('Price: ' + stock_fundament['Price'])

# If not available, print error message
except:
     print('No data available')
    
# Calculate the time taken for the entire scraping operation
end = time()
print('Time taken: ' + str(round(end - start, 2)) + 's')
