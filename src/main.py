from parser import Parser
from payments import Payments
import sys

def process_payment(data_line):
    out_str=""
    employee_data=Parser(data_line)
    
    if (employee_data.valid):
        payments=Payments()
        total_payment=int(Payments().calculate_employee_payment(employee_data.shifts))
        out_str = 'The amount to pay {} is: {} USD'.format(employee_data.employee, str(total_payment))
    else:
        out_str = "Error in data for employee {}".format(employee_data.employee)
    return out_str

if __name__ == '__main__':
    if (len(sys.argv)==2):
        data_file=sys.argv[1]
        with open(data_file, 'r') as file:
            for (index,line) in enumerate(file):
                data=line.strip()
                output=process_payment(data)
                print(output)
    else:
        print ("Usage: python main.py datafile")
                