class Employee:
	def __init__(self,eno,ename,eaddr):
		self.eno = eno
		self.ename = ename
		self.eaddr = eaddr
	def display(self):
		print(self.eno,'\t',self.ename,'\t',self.eaddr)