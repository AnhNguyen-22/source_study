class Employee:
    def __init__(self, employeeID=None,employeeCode=None, Name=None, Phone =None,Email=None,isdeleted=None):
        self.ID=employeeID
        self.employeeCode=employeeCode
        self.Name=Name
        self.Phone=Phone
        self.Email=Email
        self.isdeleted=isdeleted
    def __str__(self):
        info="{}\t{}\t{}\t{}\t{}".format(self.ID, self.Name,self.Phone,self.Email, self.employeeCode,self.isdeleted)