from params import *
from shift import Shift
from helpers import convert_time

class Payments:

    def calculate_payment(self, start_time, end_time, hour_cost):
        if (end_time==0):
            end_time=24*3600    #midnignt
        hours_worked=(end_time-start_time)/3600.0
        payment=hours_worked*hour_cost
        return payment
    
    def calculate_total_payment(self, day, start_hour, end_hour):
        shift=Shift(start_hour, end_hour)
        hour_cost=standard_hour_cost
        if day in weekend_days:
            hour_cost=weekend_hour_cost

        arrival = shift.time_in
        departure = shift.time_out
        hourly_cost = hour_cost[arrival.schedule]
        if arrival.schedule == departure.schedule:
            return self.calculate_payment(arrival.time, departure.time, hourly_cost)
        else:
            payment = self.calculate_payment(arrival.time,arrival.closing_hour,hourly_cost)
            arrival_schedule_index = day_schedules.index(arrival.schedule)
            for schedule in day_schedules[arrival_schedule_index+1:]:
                hourly_cost = hour_cost[schedule]
                
                if schedule == departure.schedule:
                    return payment + self.calculate_payment(departure.opening_hour, departure.time,hourly_cost)
                else:
                    init_time = convert_time(starting_hours[schedule])
                    end_time = convert_time(closing_hours[schedule])
                    payment = payment + self.calculate_payment(init_time,end_time,hourly_cost)
                    
    def calculate_employee_payment(self, employee_shifts):
        total_payment=0
        for shift in employee_shifts:
            total_payment+=self.calculate_total_payment(shift[1], shift[2], shift[3])
        return total_payment