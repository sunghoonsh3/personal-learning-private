import yfinance as yf
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# Replace with your FRED API key
api_key = 'efa9adb92fd704ecc81a28026d990871'
fred = Fred(api_key=api_key)

# Get CPI data, which is in a Pandas Series (a single column with labels)
cpi_data = fred.get_series('CPIAUCSL')

# Convert to DataFrame with a proper column name (which is two-dimensional)
cpi_df = pd.DataFrame(cpi_data, columns=['CPI'])
cpi_df.index = pd.to_datetime(cpi_df.index)




transactions = []

stock_name = input("Enter the stock name (or type 'done' to finish): ")
repeat_purchase = input("Have you purchased this stock more than once? \nIf yes, please type 'y'. If not, please type 'n': ")


transaction = {'stock_name': stock_name}

# Loop to collect multiple entries
if (repeat_purchase = 'y'):
    purchase_price = float(input(f"Enter the {stock_name} purchase price: "))
    sale_date = input("Enter the sale date (YYYY-MM-DD): ")
    sale_price = float(input(f"Enter the {stock_name} sale price: "))

    # Store each transaction as a dictionary
    transaction = {
        'purchase_price': purchase_price,
        'sale_date': sale_date,
        'sale_price': sale_price
    }
    transactions.append(transaction)

# Example usage
for t in transactions:
    print(t)


# # User inputs
# stock_name = input("Enter the stock name: ")
# repeat_purchase = input("Have you purchased this stock more than once? \nIf yes, please type 'y'. If not, please type 'n': ")
# purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")


# print(type(repeat_purchase))

# purchase_price = float(input(f"Enter the {stock_name} purchase price: "))
# sale_date = input("Enter the sale date (YYYY-MM-DD): ")
# sale_price = float(input(f"Enter the {stock_name} sale price: "))

# # Define purchase and sale dates1
# purchase_date = '2010-10-01'
# sale_date = '2022-10-01'

# # # Get stock prices on the purchase and sale dates
# purchase_price = stock_data.loc[purchase_date, 'Adj Close']

# print(purchase_price)

# sale_price = stock_data.loc[sale_date, 'Adj Close']

# # Calculate nominal return
# nominal_return = (sale_price - purchase_price) / purchase_price

# # Get CPI values on the purchase and sale dates
# purchase_cpi = cpi_df.loc[purchase_date, 'CPI']
# sale_cpi = cpi_df.loc[sale_date, 'CPI']

# # Calculate cumulative inflation
# cumulative_inflation = (sale_cpi - purchase_cpi) / purchase_cpi

# # Adjust nominal return for inflation to get real return
# real_return = (1 + nominal_return) / (1 + cumulative_inflation) - 1

# # Print results
# print(f"Stock Purchase Date: {purchase_date}")
# print(f"Stock Sale Date: {sale_date}")
# print(f"Purchase Price: ${purchase_price:.2f}")
# print(f"Sale Price: ${sale_price:.2f}")
# print(f"Nominal Return: {nominal_return:.2%}")
# print(f"Cumulative Inflation: {cumulative_inflation:.2%}")
# print(f"Real Return (Inflation Adjusted): {real_return:.2%}")

# # Plotting the data
# plt.figure(figsize=(14, 7))

# # Plot stock prices
# plt.plot(stock_data.index, stock_data['Adj Close'], label='Stock Price', color='blue')

# # Annotate purchase and sale points
# plt.scatter([purchase_date, sale_date], [purchase_price, sale_price], color='red')
# plt.text(purchase_date, purchase_price, f'Buy: ${purchase_price:.2f}', ha='right', fontsize=10, color='red')
# plt.text(sale_date, sale_price, f'Sell: ${sale_price:.2f}', ha='left', fontsize=10, color='red')

# # Add labels and title
# plt.xlabel('Date')
# plt.ylabel('Adjusted Close Price')
# plt.title(f'{stock_symbol} Stock Performance with Nominal and Real Returns')
# plt.legend()

# # Show plot
# plt.grid(True)
# plt.show()

# # Plot returns
# plt.figure(figsize=(14, 7))
# dates = [purchase_date, sale_date]
# nominal_returns = [0, nominal_return]
# real_returns = [0, real_return]

# plt.plot(dates, nominal_returns, label='Nominal Return', marker='o', color='green')
# plt.plot(dates, real_returns, label='Real Return (Inflation Adjusted)', marker='o', color='orange')

# # Add labels and title
# plt.xlabel('Date')
# plt.ylabel('Returns')
# plt.title('Nominal vs Real Returns')
# plt.legend()

# # Show plot
# plt.grid(True)
# plt.show()

################################################################################################

# import yfinance as yf
# import pandas as pd
# from fredapi import Fred

# # Replace with your FRED API key
# api_key = 'efa9adb92fd704ecc81a28026d990871'
# fred = Fred(api_key=api_key)

# def get_cpi(date):
#     """
#     Fetch CPI data from FRED for the given date.
#     Assumes CPI data is available for the first day of the month.
#     """
#     date_first = pd.to_datetime(date).replace(day=1)
#     cpi_data = fred.get_series('CPIAUCSL', start=date_first, end=date_first)
#     return cpi_data.iloc[0] if not cpi_data.empty else None

# # def calculate_real_return(purchase_price, sale_price, purchase_cpi, sale_cpi):
# #     nominal_return = (sale_price - purchase_price) / purchase_price
# #     cumulative_inflation = (sale_cpi - purchase_cpi) / purchase_cpi
# #     real_return = (1 + nominal_return) / (1 + cumulative_inflation) - 1
# #     return nominal_return, real_return

# # def get_sp500_data(purchase_date, sale_date):
# #     """
# #     Fetch S&P 500 data from Yahoo Finance for the given dates.
# #     """
# #     sp500 = yf.Ticker("^GSPC")
# #     sp500_data = sp500.history(start=purchase_date, end=sale_date)
# #     purchase_sp500 = sp500_data.loc[purchase_date, 'Close']
# #     sale_sp500 = sp500_data.loc[sale_date, 'Close']
# #     return purchase_sp500, sale_sp500

# def main():
#     # User inputs
#     stock_name = input("Enter the stock name: ")
#     purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
#     purchase_price = float(input(f"Enter the {stock_name} purchase price: "))
#     sale_date = input("Enter the sale date (YYYY-MM-DD): ")
#     sale_price = float(input(f"Enter the {stock_name} sale price: "))

#     # Fetch S&P 500 data from Yahoo Finance
#     purchase_sp500, sale_sp500 = get_sp500_data(purchase_date, sale_date)

#     # Fetch CPI data from FRED
#     purchase_cpi = get_cpi(purchase_date)
#     sale_cpi = get_cpi(sale_date)

#     if purchase_cpi is None or sale_cpi is None:
#         print("Error: Unable to fetch CPI data for the provided dates.")
#         return

#     # Calculate returns
#     stock_nominal_return, stock_real_return = calculate_real_return(purchase_price, sale_price, purchase_cpi, sale_cpi)
#     sp500_nominal_return, sp500_real_return = calculate_real_return(purchase_sp500, sale_sp500, purchase_cpi, sale_cpi)

#     # Display results
#     print(f"\nResults for {stock_name} from {purchase_date} to {sale_date}:")
#     print(f"Nominal Return: {stock_nominal_return:.2%}")
#     print(f"Real Return (Inflation Adjusted): {stock_real_return:.2%}\n")

#     print(f"S&P 500 Comparison:")
#     print(f"Nominal Return: {sp500_nominal_return:.2%}")
#     print(f"Real Return (Inflation Adjusted): {sp500_real_return:.2%}")

# if __name__ == "__main__":
#     main()