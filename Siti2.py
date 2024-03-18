# Set Original price
Wardah = 100000
Lipstic = 160000
Maskara = 200000

# Set stock items
Wardah_Stock = 10
Lipstic_Stock = 5
Maskara_Stock = 3

# Set Price Sell
Wardah_Price = Wardah + (Wardah * 10/100)
Lipstic_Price = Lipstic + (Lipstic * 10/100)
Maskara_Price = Maskara + (Maskara * 10/100)

print()
print("=== Product Original Price List ===")
print(f"1. Wardah = {Wardah:,}\n2. Lipstic = {Lipstic:,}\n3. Maskara = {Maskara:,}")
print()

# Amount Profit
print("=== Amount Profit ===")
print(f"1. Wardah = {Wardah * (10/100):,}")
print(f"2. Lipstic = {Lipstic * (10/100):,}")
print(f"3. Maskara = {Maskara * (10/100):,}")
print()

# Price Sell Product
print("=== List Product ===")
print(f"1. Wardah|Price: {Wardah_Price:,}|Stock: {Wardah_Stock}\n2. Lipstic|Price: {Lipstic_Price:,}|Stock: {Lipstic_Stock}\n3. Maskara|Price: {Maskara_Price:,}|Stock: {Maskara_Stock}")
print()

# Selling

Name_Goods = int(input("Enter The Product Number : "))
Much = int(input("How Much Do You Want To Buy : "))

if Name_Goods == 1:
    if Much <= Wardah_Stock :
        print()
        print("===== Receipt =====")
        print("You Buy Wardah : " + str(Much) + " " + "Pcs")
        print(f"Price Wardah{3*" "}: Rp.{Wardah_Price:,}/pcs")
        print(19*"=")
        print(f"Total{10*" "}: Rp.{Much * (Wardah + (Wardah * 10/100)):,}")
        print()
        print(f"#Amount Profit {Much * (Wardah * 10/100):,}")
        print()
    else :
        print("Insufficient Stock")
elif Name_Goods == 2: 
     if Much <= Lipstic_Stock :
        print()
        print("===== Receipt =====")
        print("You Buy Lipstic : " + str(Much) + " " + "Pcs")
        print(f"Price Lipstic{3*" "}: Rp.{Lipstic_Price:,}/pcs")
        print(19*"=")
        print(f"Total{11*" "}: Rp.{Much * (Lipstic + (Lipstic * 10/100)):,}")
        print()
        print(f"#Amount Profit {Much * (Lipstic * 10/100):,}")
        print()
     else :
        print("Insufficient Stock")
         
elif Name_Goods == 3:
    if Much <= Maskara_Stock :
        print()
        print("===== Receipt =====")
        print("You Buy Maskara : " + str(Much) + " " + "Pcs")
        print(f"Price Maskara{3*" "}: Rp.{Maskara_Price:,}/pcs")
        print(19*"=")
        print(f"Total{11*" "}: Rp.{Much * (Maskara + (Maskara * 10/100)):,}")
        print()
        print(f"#Amount Profit {Much * (Maskara * 10/100):,}")
        print()
    else :
        print("Insufficient Stock")
else :
    print("Product Not Found")
print()
