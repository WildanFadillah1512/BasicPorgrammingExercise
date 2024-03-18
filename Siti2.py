Name_Goods = str(input("Enter The Item Name : "))
Price_Goods = float(input("Enter The Price Of The Item : "))
Stock_Goods = int(input("Enter The Stock : "))

Price = (Price_Goods * (10/100)) 
Profit = Price + Price_Goods
Profit_item = Stock_Goods * Price
Profit_amount = Profit * Stock_Goods
print()
print(f"Transaction Amount is :", Stock_Goods)
print()
print(f"Profit per Item :{Price:,}")
print()
print(f"Selling Price : {Profit:,}")
print()
print(f"Profit Amount :{Profit_item:,}")
print()
print(f"Amount of Money :{Profit_amount:,}")
print()