import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    current_price = ticker.history(period="1d")['Close'][0]
    return current_price

def calculate_portfolio(portfolio_data):
    total_value = 0
    portfolio = []
    
    for data in portfolio_data:
        symbol, avg_price, amount = data['symbol'], data['avg_price'], data['amount']
        current_price = get_stock_data(symbol)
        stock_value = current_price * amount
        total_value += stock_value
        
        roi = ((current_price - avg_price) / avg_price) * 100
        portfolio.append({
            'symbol': symbol,
            'amount': amount,
            'avg_price': avg_price,
            'current_price': current_price,
            'stock_value': stock_value,
            'roi': roi
        })
    
    return portfolio, total_value

def display_portfolio(portfolio, total_value):
    labels = []
    sizes = []
    for stock in portfolio:
        labels.append(f"{stock['symbol']} ({stock['roi']:.2f}% ROI)")
        sizes.append(stock['stock_value'])
    
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Portfolio Distribution')
    plt.show()

    print("\nPortfolio Details:")
    for stock in portfolio:
        print(f"Symbol: {stock['symbol']}")
        print(f" - Amount: {stock['amount']}")
        print(f" - Average Purchase Price: ${stock['avg_price']:.2f}")
        print(f" - Current Price: ${stock['current_price']:.2f}")
        print(f" - Value: ${stock['stock_value']:.2f}")
        print(f" - ROI: {stock['roi']:.2f}%\n")


# this logice needs to be fixed. there is a problem with stock symbol handling and calculating the target value
def calculate_rebalance(portfolio, total_value, new_investment, target_distribution):
    new_allocation = {}
    for stock in portfolio:
        symbol = stock['symbol']
        current_value = stock['stock_value']
        target_value = total_value * (target_distribution[symbol] / 100)
        additional_investment = max(0, target_value - current_value)
        new_allocation[symbol] = additional_investment
    
    total_additional_investment = sum(new_allocation.values())
    
    for symbol, amount in new_allocation.items():
        new_allocation[symbol] = (amount / total_additional_investment) * new_investment
    
    for stock in portfolio:
        symbol = stock['symbol']
        stock['new_investment'] = new_allocation[symbol]
        stock['new_shares'] = stock['new_investment'] / stock['current_price']
    
    return portfolio

def display_rebalance_plan(portfolio):
    print("\nRebalance Plan:")
    for stock in portfolio:
        print(f"Symbol: {stock['symbol']}")
        print(f" - Current Value: ${stock['stock_value']:.2f}")
        print(f" - New Investment: ${stock['new_investment']:.2f}")
        print(f" - New Shares to Buy: {stock['new_shares']:.2f}\n")

def main():
    portfolio_data = []
    
    while True:
        symbol = input("Enter stock symbol: ").upper()
        avg_price = float(input(f"Enter average purchase price for {symbol}: "))
        amount = int(input(f"Enter amount of {symbol} purchased: "))
        print("\n")
        
        portfolio_data.append({
            'symbol': symbol,
            'avg_price': avg_price,
            'amount': amount
        })
        
        more = input("Do you want to add another stock? (y/n): ").lower()
        print("\n")
        if more != 'y':
            break

    portfolio, total_value = calculate_portfolio(portfolio_data)
    display_portfolio(portfolio, total_value)
    
    rebalance = input("Do you want to rebalance your portfolio with a new investment? (yes/no): ").lower()
    
    if rebalance == 'yes':
        target_distribution = {}
        
        while True: 
            for stock in portfolio:
                symbol = stock['symbol']
                target_percentage = float(input(f"Enter target percentage for {symbol}: "))
                target_distribution[symbol] = target_percentage
            
            # need to ask about a new investment. what's the symbol? and how much percentage would you want it to be?    
            symbol = input("Enter the symbol for new investment: ").upper()
            target_percentage = float(input(f"Enter target percentage for {symbol}: "))
            target_distribution[symbol] = target_percentage
            
            # check if the percentage target meets 100%
                
            percentage_total = 0
            for value in target_distribution.values():
                percentage_total += value
            
            if percentage_total != 100:
                print("Portfolio must be at 100% at all times\n")
            
            else:
                break
            
        
        new_investment = float(input("Enter the amount you want to invest: "))
        portfolio = calculate_rebalance(portfolio, total_value, new_investment, target_distribution)
        display_rebalance_plan(portfolio)

if __name__ == "__main__":
    main()






# # Replace with your FRED API key
# api_key = 'efa9adb92fd704ecc81a28026d990871'
# fred = Fred(api_key=api_key)

# # Get CPI data, which is in a Pandas Series (a single column with labels)
# cpi_data = fred.get_series('CPIAUCSL')

# # Convert to DataFrame with a proper column name (which is two-dimensional)
# cpi_df = pd.DataFrame(cpi_data, columns=['CPI'])
# cpi_df.index = pd.to_datetime(cpi_df.index)

# 1. I want the user to be able to see their portfolio easily and be able to rebalance it easily. 
# I want the user to be basically enter the amount of money they would like to put to balance the money.




# # Replace with your FRED API key
# api_key = 'efa9adb92fd704ecc81a28026d990871'
# fred = Fred(api_key=api_key)

# # Get CPI data, which is in a Pandas Series (a single column with labels)
# cpi_data = fred.get_series('CPIAUCSL')

# # Convert to DataFrame with a proper column name (which is two-dimensional)
# cpi_df = pd.DataFrame(cpi_data, columns=['CPI'])
# cpi_df.index = pd.to_datetime(cpi_df.index)

# 1. I want the user to be able to see their portfolio easily and be able to rebalance it easily. 
# I want the user to be basically enter the amount of money they would like to put to balance the money.




