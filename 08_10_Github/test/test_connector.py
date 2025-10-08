import mysql.connector

server="localhost"
port=3306
database="k23416_retail"
user="root"
password="Hoanganh22"

conn=mysql.connector.connect(
    host=server, port=port, database=database, user=user, password=password)
print("ok")

print("CRUD")
#Đăng nhập cho customer:
def login_customer(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
          "where Email='"+email +"' and Password ='"+pwd+"'"
    print(sql)
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed!")
    cursor.close()

def login_employee(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee " \
          "where Email=%s and Password=%s"
    val=(email,pwd)
    cursor.execute(sql, val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed!")
    cursor.close()

