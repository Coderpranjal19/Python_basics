user_number1 = input("enter no: ")
user_number2 = input("enter no: ")
user_number3 = input("enter no: ")
user_number4 = input("enter no: ")

if (user_number1>user_number2):
    bigger = user_number1
else:
    bigger = user_number2

if (user_number3>user_number4):
    bigger2 = user_number3
else:
    bigger2 = user_number4

if (bigger>bigger2):
    print(str(bigger) + " is greatest")
else:
    print(str(bigger2) + " is greatest")       