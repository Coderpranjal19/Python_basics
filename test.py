class Customer:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.name},{self.dob}"
        
    def m1(self):
    	print(self.name,'\t',self.dob)
    
    
        
c = Customer("pranjal",191199)
c.m1()
print(c)