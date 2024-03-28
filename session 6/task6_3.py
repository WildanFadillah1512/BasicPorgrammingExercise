people_name = str(input("input your name :"))
people_age = int(input("how old are you? "))
if people_age > 0 and people_age < 12 :
    print("Your Age Group is : Child")
elif people_age > 13 and people_age < 19 :
    print("Your Age Group is : Teenager")
elif people_age > 20 :
    print("Your Age Group is : Teenager")
else :
    print("Your Age is unindentified")
