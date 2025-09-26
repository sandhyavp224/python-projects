prices={
    "AAPL": 180 ,
    "TSLA": 250 ,
    "GOOG": 140 ,
    "MSFT": 330
}
portfolio = {}
while True:
    stock=input("Enter stock symbol ( or 'done' to finish): ").upper()
    if stock is 'DONE':
        break
    if stock in prices:
        qty=int(input(f"Enter quantity for {stock} : "))
        portfolio[stock]=portfolio.get(stock , 0 ) + qty

    else:
        print("Stock not g=found in price list , better luck next time")

total_value=0
print("\n Your portfolio: ")
for stock , qty in portfolio.items():
    value = prices[stock] * qty
    print(f"{stock} : {qty} shares X {prices[stock]} = {value}")
    total_value += value
    print(f"Total Investment: {total_value}")
    save = input("Save results to file? (y/n): ").lower()

if save == 'y':
    with.open("Portfolia.csv" , "w") as file:
        file.write("Stock")
