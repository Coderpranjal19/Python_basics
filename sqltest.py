import pymysql
con = pymysql.connect(host='localhost', database='pranjaldb', user='root', password='Patel@19')
cursor = con.cursor()
cursor.execute("insert into employees (eno, ename, esal, eaddress) values (555,'madhu',3000,'hyd')")
con.commit()
print('records updated successfully')
cursor.execute('select * from employees')
data = cursor.fetchall()
print(data)
if cursor:
    cursor.close()
if con:
    con.close()