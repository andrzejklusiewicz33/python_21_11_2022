class Author:
    first_name=None
    last_name=None
    email=None
    phone_number=None
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number

    def __str__(self):
        #return f"first_name={self.first_name}, last_name={self.last_name}"
        return str(self.__dict__)
    # def __init__(self):
    #     print('DUPA!!!!!!!!!')