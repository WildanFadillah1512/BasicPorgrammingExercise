number_1 = float(input("input your number : "))
number_2 = float(input("input your number : "))

operation = f"""
1. Sum
2. Substrack
3. Multiply
4. Division
"""
print(operation)
operation_2 = int(input("click the operation :"))
if operation_2 == 1 :
    print("Result your operation is :" ,{number_1 + number_2})
elif operation_2 == 2 :
    print("Result your operation is :" ,{number_1 - number_2})
elif operation_2 == 3 :
    print("Result your operation is :" ,{number_1 * number_2})
elif operation_2 == 4 :
    print("Result your operation is :" ,{number_1 / number_2})
else :
    print("Wrong input please try again")