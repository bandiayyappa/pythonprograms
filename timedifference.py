from datetime import datetime as dt
time1 = input('Enter time in HH:MM:SS').strip()
time2 = input('Enter time in HH:MM:SS').strip()
format_ = '%H:%M:%S'

def time_difference(time1,time2):
    try:
        tdelta = dt.strptime(time2, format_) - dt.strptime(time1, format_)
        return tdelta
    except Exception as e:
        return 'Error--->',e
print(time_difference(time1,time2))

