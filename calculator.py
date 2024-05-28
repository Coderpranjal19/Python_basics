import math
class calculator:
    def add(self,var1,var2):
        var3 = var1 + var2
        return var3
    def sub(self,var1,var2):
        var3 = var1 - var2
        return var3
    def multiply(self,var1,var2):
        var3 = var1 * var2
        return var3
    def divide(self,var1,var2):
        var3 = var1 / var2
        return var3

pranjal = calculator()
print("enter your choice: ")
print("1.add 2.sub 3.multiply 4.divide")
choice = input()
loop = 'n'
while loop == 'n':
    if choice.isnumeric() and (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
         loop = 'y'
         print("enter 1st number: ")
         inp1 = float(input())
         print("enter 2nd number: ")
         inp2 = float(input())
         out=0.0
         if choice == '1':
            out = pranjal.add(inp1,inp2)
            print("sum of " + str(inp1) + "+" + str(inp2) + " is " + str(out))
         elif choice == '2':
            out = pranjal.sub(inp1,inp2)
            print("sub of " + str(inp1) +"-"+ str(inp2) + " is " + str(out))
         elif choice == '3':
            out = pranjal.multiply(inp1,inp2)
            print("multiply of " + str(inp1) +"*"+ str(inp2) + " is " + str(out))
         else:
            out = pranjal.divide(inp1,inp2)
            print("division of " + str(inp1) +"/"+ str(inp2) + " is " + str(out))
    else:
        print("entered number is invalid,please try again")
        choice = input()
