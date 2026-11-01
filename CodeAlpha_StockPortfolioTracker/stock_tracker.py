
stock_prices = {
    "apple": 200,
    "google": 150,
    "microsoft": 400,
    "amazon": 180,
    "tesla": 250
}

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

total_investment = 0
portfolio = []

while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).strip().lower()

    if stock_name == "done":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print("Stock price:", price)
    print("Investment for this stock:", investment)

print("\n===== Portfolio Summary =====")

if not portfolio:
    print("No stocks were added.")
else:
    for item in portfolio:
        print(
            item["stock"].title(),
            "| Quantity:", item["quantity"],
            "| Price:", item["price"],
            "| Investment:", item["investment"]
        )

    print("\nTotal investment:", total_investment)

    save = input("Save report to a text file? (yes/no): ").strip().lower()

    if save == "yes":
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Report\n")
            file.write("======================\n")

            for item in portfolio:
                file.write(
                    f"{item['stock'].title()} | "
                    f"Quantity: {item['quantity']} | "
                    f"Price: {item['price']} | "
                    f"Investment: {item['investment']}\n"
                )

            file.write(f"\nTotal investment: {total_investment}\n")

        print("Report saved as portfolio_report.txt")

print("\nThank you for using Stock Portfolio Tracker!")
