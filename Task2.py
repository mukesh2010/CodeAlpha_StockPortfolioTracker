import csv

stock_prices = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "AMZN": 130.0,
    "MSFT": 320.0,
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Enter stock symbol and number of shares.")
print("Type 'done' when you are finished.\n")

while True:
    symbol = input("Stock symbol (e.g., AAPL, TSLA) or 'done': ").upper().strip()

    if symbol == "DONE":
        break

    if symbol not in stock_prices:
        print("Unknown stock symbol. Available symbols:")
        print(", ".join(stock_prices.keys()))
        continue

    try:
        shares = float(input(f"Number of shares for {symbol}: ").strip())
        if shares <= 0:
            print("Please enter a positive number of shares.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[symbol] = portfolio.get(symbol, 0) + shares

if not portfolio:
    print("\nNo stocks entered.")
else:
    print("\nYour Portfolio:")
    total_value = 0.0

    for symbol, shares in portfolio.items():
        price = stock_prices[symbol]
        value = shares * price
        total_value += value
        print(f"{symbol}: {shares} shares at ${price:.2f} each -> ${value:.2f}")

    print(f"\nTotal investment value: ${total_value:.2f}")

    save_choice = input("\nSave portfolio to CSV file? (y/n): ").lower().strip()
    if save_choice == "y":
        filename = "portfolio.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Shares", "Price", "Value"])
            for symbol, shares in portfolio.items():
                price = stock_prices[symbol]
                value = shares * price
                writer.writerow([symbol, shares, price, value])
        print(f"Portfolio saved to {filename}.")
