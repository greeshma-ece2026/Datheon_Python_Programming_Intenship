import csv
import os

print("=" * 45)
print("     STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 45)

portfolio = []

while True:
    ticker = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if not ticker:
        print("Please enter a valid stock symbol.")
        continue

    try:
        buy_price = float(input("Enter buying price per share: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

        current_price = float(input("Enter current price per share: "))

        if current_price <= 0:
            print("Current price must be positive.")
            continue

        investment = buy_price * quantity
        market_value = current_price * quantity
        profit_loss = market_value - investment
        percentage = (profit_loss / investment) * 100

        portfolio.append({
            "Ticker": ticker,
            "Buy Price": buy_price,
            "Current Price": current_price,
            "Quantity": quantity,
            "Investment": investment,
            "Market Value": market_value,
            "Profit/Loss": profit_loss,
            "Gain/Loss (%)": percentage
        })

    except ValueError:
        print("Invalid input! Please enter numbers for prices and quantity.")

if portfolio:
    total_investment = sum(item["Investment"] for item in portfolio)
    total_value = sum(item["Market Value"] for item in portfolio)
    total_profit = total_value - total_investment

    print("\n" + "=" * 45)
    print("             PORTFOLIO SUMMARY")
    print("=" * 45)

    for item in portfolio:
        print(f"\nStock: {item['Ticker']}")
        print(f"Investment: Rs. {item['Investment']:.2f}")
        print(f"Market Value: Rs. {item['Market Value']:.2f}")
        print(f"Profit/Loss: Rs. {item['Profit/Loss']:.2f}")
        print(f"Gain/Loss: {item['Gain/Loss (%)']:.2f}%")

    print("\nTotal Investment: Rs.", round(total_investment, 2))
    print("Total Market Value: Rs.", round(total_value, 2))
    print("Total Profit/Loss: Rs.", round(total_profit, 2))

    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=portfolio[0].keys())
        writer.writeheader()
        writer.writerows(portfolio)

    print("\nReport saved as portfolio_summary.csv")
else:
    print("\nNo stock records entered.")

input("\nPress Enter to exit...")