from datetime import datetime as dt

def date_difference(d1, d2):
    try:
        format_ = "%Y-%m-%d"
        date1 = dt.strptime(d1, format_)
        date2 = dt.strptime(d2, format_)
    except ValueError:
        return 'wrong data'
    return (date2 - date1)


print(date_difference('2019-04-1','2019-04-15'))


