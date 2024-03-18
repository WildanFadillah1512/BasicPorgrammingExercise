Name_Goods = str(input("Enter The Item Name : "))
Price_Goods = float(input("Enter The Price Of The Item : "))
Stock_Goods = int(input("Enter The Stock : "))

Profit = (Price_Goods * (10/100)) 
Selling = Profit + Price_Goods
Profit_amount = Stock_Goods * Profit
Money = Selling * Stock_Goods
print()
print(f"Transaction Amount is :", Stock_Goods)
print()
print(f"Profit per Item :{Profit:,}")
print()
print(f"Selling Price : {Selling:,}")
print()
print(f"Profit Amount :{Profit_amount:,}")
print()
print(f"Amount of Money :{Money:,}")
print()