Name_Goods = str(input("Enter The Item Name : "))
Price_Goods = float(input("Enter The Price Of The Item :"))
Stock_Goods = int(input("Enter The Stock : "))

Price = (Price_Goods * (10/100)) 
Profit = Price + Price_Goods
Profit_item = Stock_Goods * Price
Profit_amount = Profit * Stock_Goods
print()
print("Transaction Amount is :", Stock_Goods)
print()
print("Profit per Item :", Price)
print()
print("Selling Price :", Profit)
print()
print("Profit Amount :", Profit_item)
print()
print("Amount of Money :", Profit_amount)
print()