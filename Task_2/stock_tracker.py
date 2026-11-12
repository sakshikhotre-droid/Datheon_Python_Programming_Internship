
import csv
import os

filename = "portfolio.csv"

stock_name = input("Enter Stock Name: ")
buying_price = float(input("Enter Buying Price: "))
quantity = int(input("Enter Quantity: "))
current_price = float(input("Enter Current Price: "))

investment = buying_price * quantity
current_value = current_price * quantity
profit_loss = current_value - investment

print("\n===== STOCK PORTFOLIO REPORT =====")
print("Stock Name:", stock_name)
print("Total Investment:", investment)
print("Current Value:", current_value)

if profit_loss > 0:
    print("Profit:", profit_loss)
elif profit_loss < 0:
    print("Loss:", abs(profit_loss))
else:
    print("No Profit, No Loss")

file_exists = os.path.exists(filename)

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Stock Name",
            "Buying Price",
            "Quantity",
            "Current Price",
            "Investment",
            "Current Value",
            "Profit/Loss"
        ])

    writer.writerow([
        stock_name,
        buying_price,
        quantity,
        current_price,
        investment,
        current_value,
        profit_loss
    ])

print("\nStock data saved successfully in portfolio.csv!")
