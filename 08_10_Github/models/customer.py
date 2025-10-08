class Customer:
    def __init__(self, customerID=None, name=None, phone =None,email=None,password=None,isdeleted=None):
        self.ID=customerID
        self.Name=name
        self.Phone=phone
        self.Email=email
        self.Password=password
        self.isdeleted=isdeleted
    def __str__(self):
        info="{}\t{}\t{}\t{}\t{}".format(self.ID, self.Name,self.Phone,self.Email, self.Password,self.isdeleted)