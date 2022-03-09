from params import week_days, weekend_days
from datetime import datetime
from helpers import convert_time

class Parser:
    def __init__(self, input_data=''):
        self.input_data=input_data
        self.valid=True

        if (input_data):
            self.employee=self.get_employee()

            employee_shifts=[]
            for shift in self.get_shifts():
                work_shift=self.get_work_shift(shift)
                if (work_shift[0]==False):
                    self.valid=False
                employee_shifts.append(self.get_work_shift(shift))
                

            self.shifts=employee_shifts
        else:
            valid=False
    
    def get_employee(self):
        employee=self.input_data.split('=')[0]
        return employee

    def get_shifts(self):
        shifts=self.input_data.split('=')[1].split(',')
        return shifts
    
    def get_workdays(self):
        days_list=[]
        work_shifts=self.input_data.split('=')[1].split(',')
        for work_shift in work_shifts:
            work_day=work_shift[0:2]
            days_list.append(work_day)
        return days_list

    def get_work_shift(self, shift):
        valid_day=False
        valid_time=False
        valid_input=False

        work_day=shift[0:2]
        work_time=shift[2:].split('-')

        if (work_day in week_days or work_day in weekend_days):
            valid_day=True
        
        time_start=convert_time(work_time[0])
        time_end=convert_time(work_time[1])

        if (time_end-time_start)>0:
            valid_time=True

        if (valid_day and valid_time):
            valid_input=True
        
        return (valid_input, work_day, time_start, time_end)




