class guess:
    def greatest_number(num1,num2,num3):
        if (num1>num2):
            if(num1>num3):
                return num1
            else:
                return num3
        else:
            if(num2>num3):
                return num2
            else:
                return num3
print("please type 1st no:")
inp1 = input()
print("please type 2nd no:")
inp2 = input()
print("please type 3rd no:")
inp3 = input()


m = guess.greatest_number(inp1,inp2,inp3)

print("Greatest number is :" + str(m))

    
    
        

