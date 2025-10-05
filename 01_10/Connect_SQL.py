import mysql.connector

server="localhost"
port=3306
database="studentmanagement"
user="root"
password="Hoanganh22"

conn=mysql.connector.connect(
    host=server, port=port, database=database, user=user, password=password)
'''
cursor=conn.cursor()
sql="select * from student"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<5} {3:<10}'
print(align.format("idstudent", "Code", "Name", "Age"))
for item in dataset:
    idstudent = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(idstudent, code, name, age))

cursor.close()

cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where Age>=22 and Age<=26 " \
    "order by Age desc "
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where ID=1 "

cursor.execute(sql)

dataset=cursor.fetchone()
if dataset!=None:
    id,code,name,age,avatar,intro=dataset
    print("Id=",id)
    print("code=",code)
    print("name=",name)
    print("age=",age)

cursor.close()
#câu lệnh limit:
print("PAGING!!!!!")
cursor = conn.cursor()
sql="SELECT count(*) FROM student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit=3
step=3
for offset in range(0,rowcount,step):
    sql=f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align='{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id=item[0]
        code=item[1]
        name=item[2]
        age=item[3]
        avatar=item[4]
        intro=item[5]
        print(align.format(id,code,name,age))

cursor.close()
#thêm một loạt hàng cho bảng student
cursor=conn.cursor()
sql="insert into student(Code,Name,Age) values(%s,%s,%s)"
val=[("sv07","Nhi",19),
     ("sv08","Trà",18),
     ("sv09","Diệu",25),
     ("sv10","Obama",26)]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record inserted")
cursor.close()


#cập nhật tên sinh viên
cursor=conn.cursor()
sql="update student set Name='Hoàng Anh' where idstudent=1"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount,"record updated")
#hoặc cách khác:
cursor = conn.cursor()
sql="update student set name=%s where Code=%s"
val=('Hoàng Lão Tà','sv09')

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record(s) affected")

#xóa dữ liệu mysql
conn=mysql.connector.connect(
    host=server, port=port, database=database, user=user, password=password)
cursor=conn.cursor()
sql="delete from student where Code='sv09'"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount,"record deleted")
#hoặc
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql = "DELETE from student where ID=%s"
val = (13,)

cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount," record(s) affected")
'''


