from domain import *
def get_all():
    e1 = Employee(1,'Andrzej','Klusiewicz','1111','Python Developer')
    e2 = Employee(2, 'Twoja', 'Stara', '696969696', 'Senior operator mikrofalówki')
    e3 = Employee(3, 'Jakiś', 'Ktoś', '22222', 'Konserwator powierzchni płaskich')
    employees=[e1,e2,e3]
    return employees
    #employees=[Employee(1,'Andrzej','Klusiewicz','1111','Python Developer'),Employee(2, 'Twoja', 'Stara', '696969696', 'Senior operator mikrofalówki'),Employee(3, 'Jakiś', 'Ktoś', '22222', 'Konserwator powierzchni płaskich')]
