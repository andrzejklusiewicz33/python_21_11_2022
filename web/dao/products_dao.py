from domain import *
# def get_all():
#     p1=Product(1,'Bulbulator','robi bul bul',1111)
#     p2=Product(2,'Wihajster','takie cos z takim czyms bez takiego czegos',9999)
#     p3=Product(3,'Przyczłap do wihajstra','Takie coś że można to i tamto',100)
#     result=[p1,p2,p3]
#     return result

import dao.dao_settings as ds
import psycopg2
def get_all():
    result=[]
    with psycopg2.connect(host=ds.host,port=ds.port,database=ds.database,user=ds.user,password=ds.password) as connection:
            cursor=connection.cursor()
            cursor.execute('select * from produkty')
            for w in cursor:
                product=Product(w[0],w[1],w[2],w[3])
                result.append(product)
    return result