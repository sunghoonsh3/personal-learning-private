import yfinance as yf
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# Replace with your FRED API key
api_key = 'efa9adb92fd704ecc81a28026d990871'
fred = Fred(api_key=api_key)

# Get CPI data
cpi_data = fred.get_series('CPIAUCSL')

print(cpi_data.head())

# Convert to DataFrame with a proper column name
cpi_df = pd.DataFrame(cpi_data, columns=['CPI'])
cpi_df.index = pd.to_datetime(cpi_df.index)

# Fetch historical stock data
stock_symbol = 'AAPL'  # Example stock symbol
stock_data = yf.download(stock_symbol, start='2010-01-01', end='2024-01-01')

# Define purchase and sale dates
purchase_date = '2010-10-19'
sale_date = '2022-10-28'

# # Get stock prices on the purchase and sale dates
purchase_price = stock_data.loc[purchase_date, 'Adj Close']

print(purchase_price)

sale_price = stock_data.loc[sale_date, 'Adj Close']

# Calculate nominal return
nominal_return = (sale_price - purchase_price) / purchase_price

# Get CPI values on the purchase and sale dates
purchase_cpi = cpi_df.loc[purchase_date, 'CPI']
sale_cpi = cpi_df.loc[sale_date, 'CPI']

# Calculate cumulative inflation
cumulative_inflation = (sale_cpi - purchase_cpi) / purchase_cpi

# Adjust nominal return for inflation to get real return
real_return = (1 + nominal_return) / (1 + cumulative_inflation) - 1

# Print results
print(f"Stock Purchase Date: {purchase_date}")
print(f"Stock Sale Date: {sale_date}")
print(f"Purchase Price: ${purchase_price:.2f}")
print(f"Sale Price: ${sale_price:.2f}")
print(f"Nominal Return: {nominal_return:.2%}")
print(f"Cumulative Inflation: {cumulative_inflation:.2%}")
print(f"Real Return (Inflation Adjusted): {real_return:.2%}")

# Plotting the data
plt.figure(figsize=(14, 7))

# Plot stock prices
plt.plot(stock_data.index, stock_data['Adj Close'], label='Stock Price', color='blue')

# Annotate purchase and sale points
plt.scatter([purchase_date, sale_date], [purchase_price, sale_price], color='red')
plt.text(purchase_date, purchase_price, f'Buy: ${purchase_price:.2f}', ha='right', fontsize=10, color='red')
plt.text(sale_date, sale_price, f'Sell: ${sale_price:.2f}', ha='left', fontsize=10, color='red')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.title(f'{stock_symbol} Stock Performance with Nominal and Real Returns')
plt.legend()

# Show plot
plt.grid(True)
plt.show()

# Plot returns
plt.figure(figsize=(14, 7))
dates = [purchase_date, sale_date]
nominal_returns = [0, nominal_return]
real_returns = [0, real_return]

plt.plot(dates, nominal_returns, label='Nominal Return', marker='o', color='green')
plt.plot(dates, real_returns, label='Real Return (Inflation Adjusted)', marker='o', color='orange')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Returns')
plt.title('Nominal vs Real Returns')
plt.legend()

# Show plot
plt.grid(True)
plt.show()