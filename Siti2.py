Name_Goods = str(input("Enter The Item Name : "))
Price_Goods = float(input("Enter The Price Of The Item :"))
Stock_Goods = int(input("Enter The Stock : "))

Profit = (Price_Goods * (10/100)) + Price_Goods 
Profit_amount = Profit * Stock_Goods
print()
print("Transaction Amount is :", Stock_Goods)
print()
print("Profit per Item :", Profit)
print()
print("The Amount of Profit is :", Profit_amount)
print()