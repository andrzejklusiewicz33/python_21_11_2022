import dao.dao_settings
from domain import *
# def get_all():
#     e1 = Employee(1,'Andrzej','Klusiewicz','1111','Python Developer')
#     e2 = Employee(2, 'Twoja', 'Stara', '696969696', 'Senior operator mikrofalówki')
#     e3 = Employee(3, 'Jakiś', 'Ktoś', '22222', 'Konserwator powierzchni płaskich')
#     employees=[e1,e2,e3]
#     return employees
#     #employees=[Employee(1,'Andrzej','Klusiewicz','1111','Python Developer'),Employee(2, 'Twoja', 'Stara', '696969696', 'Senior operator mikrofalówki'),Employee(3, 'Jakiś', 'Ktoś', '22222', 'Konserwator powierzchni płaskich')]
import dao.dao_settings as ds
import psycopg2
def get_all():
    result=[]
    with psycopg2.connect(host=ds.host,port=ds.port,database=ds.database,user=ds.user,password=ds.password) as connection:
            cursor=connection.cursor()
            cursor.execute('select * from pracownicy')
            for w in cursor:
                employee=Employee(w[0],w[1],w[2],w[3],w[4])
                result.append(employee)
    return result

def get_one(id):
    with psycopg2.connect(host=ds.host, port=ds.port, database=ds.database, user=ds.user,password=ds.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from pracownicy where id_pracownika={id}')
        w=cursor.fetchone()
        employee=Employee(w[0],w[1],w[2],w[3],w[4])
        return employee

def save(employee):
    sql=f"insert into pracownicy(imie,nazwisko,telefon,stanowisko) values('{employee.first_name}','{employee.last_name}','{employee.phone_number}','{employee.position}')"
    with psycopg2.connect(host=ds.host, port=ds.port, database=ds.database, user=ds.user,password=ds.password) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

#threading
#asyncio