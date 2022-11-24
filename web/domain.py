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

class Favourites:
    film=None
    book=None

class Employee:
    employee_id=None
    first_name=None
    last_name=None
    phone_number=None
    position=None
    def __init__(self,ei,fn,ln,pn,po):
        self.employee_id=ei
        self.first_name=fn
        self.last_name=ln
        self.phone_number=pn
        self.position=po

    def __str__(self):
        return str(self.__dict__)

    def serialize(self):
        return self.__dict__



class Product:
    product_id=None
    name=None
    description=None
    price=None

    def __init__(self,pi,n,d,p):
        self.product_id=pi
        self.name=n
        self.description=d
        self.price=p

    def __str__(self):
        return str(self.__dict__)
