import mysql.connector
from models.customer import Customer
server="localhost"
port=3306
database="k23416_retail"
user="root"
password="Hoanganh22"

conn=mysql.connector.connect(
    host=server, port=port, database=database, user=user, password=password)
print("ok")

#Đăng nhập cho customer:
def login_customer(email,password):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer WHERE Email = %s AND Password = %s"
    cust=None
    cursor.execute(sql, (email, password))
    datasets=cursor.fetchone()
    if datasets!=None:
        cust=Customer(datasets[0],datasets[1],datasets[2],datasets[3],datasets[4],datasets[5])
    cursor.close()
    return cust
cust=login_customer("anh@gmail.com","qưeryriuty")
if cust==None:
    print("login failed")
else:
    print("Login successful")
    print(cust)
