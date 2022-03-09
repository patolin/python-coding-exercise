from datetime import datetime

def convert_time(time_str):
    t_format = '%H:%M'
    zero_time = datetime.strptime('00:00', t_format)
    day_time = datetime.strptime(time_str, t_format) - zero_time
    return day_time.seconds