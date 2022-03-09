from parser import Parser
from payments import Payments



if __name__ == '__main__':
    data='RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    employee_data=Parser(data)
    if (employee_data.valid):
        print (data)
        total=Payments().calculate_employee_payment(employee_data.shifts)
        print (total)
    else:
        print ("Error")



