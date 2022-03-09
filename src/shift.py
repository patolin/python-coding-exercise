from params import *
from helpers import convert_time

class Shift:

    def __init__(self, init_time, end_time):
        self.time_in = self.Schedule(init_time)
        self.time_out = self.Schedule(end_time)

    class Schedule:

        def __init__(self, time):
            self.time = time
            (self.schedule, self.opening_hour, self.closing_hour) = self.get_schedule(time)
        
        def get_schedule(self, time):
            for schedule in day_schedules:
                init_time_range=convert_time(starting_hours[schedule])
                end_time_range=convert_time(closing_hours[schedule])
                if (end_time_range==0):
                    end_time_range=24*3600 #midnignt
                if init_time_range <= time < end_time_range:
                    opening_hour = convert_time(starting_hours[schedule])
                    closing_hour = convert_time(closing_hours[schedule])
                    return (schedule, opening_hour, closing_hour)