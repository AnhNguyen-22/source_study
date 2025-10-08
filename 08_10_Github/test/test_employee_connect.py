from connectors.employee_connect import EmployeeConnect
ec=EmployeeConnect()
ec.connect()
em=ec.login("anh@gmail.com","qeryriuty")
if em==None:
    print("login failed")
else:
    print("login successful")
    print(em)
