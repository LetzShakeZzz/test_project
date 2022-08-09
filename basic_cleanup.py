from datetime import date

def saturdays_between_two_dates(start, end):
    saturdays = 0
    for i in range(min(start, end).toordinal(), max(start, end).toordinal() + 1):
        if date.fromordinal(i).weekday() == 5:
            saturdays += 1
    return saturdays

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)
print(saturdays_between_two_dates(date1, date2))

    
