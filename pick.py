import pickle,emp
f = open('emp.dat','wb')
n = int(input('Enter the number of employees:'))
for i in range(n):
	eno = int(input('Enter employee number:'))
	ename = input('Enter employee name:')
	eaddr = input('Enter employee address:')
	e = emp.Employee(eno,ename,eaddr)
	pickle.dump(e,f)
print('Employee objects pickled successfully.....')