# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 420
}

total_investment = 0

print("====== Stock Portfolio Tracker ======")

num = int(input("Enter number of different stocks: "))

for i in range(num):
    stock = input("\nEnter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Price per Share :", stock_prices[stock])
        print("Investment Value :", investment)

    else:
        print("Stock not found!")

print("\n================================")
print("Total Investment =", total_investment)
print("================================")

# Optional File Saving
file = open("portfolio.txt", "w")
file.write("Total Investment = ₹" + str(total_investment))
file.close()

print("Portfolio saved successfully!")
