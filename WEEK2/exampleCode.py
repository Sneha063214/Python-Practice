month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return (year%4==0)and((year%100!=0)or(year%400==0))

def no_of_days(year,month):
    if month>12 or month<1:
        return 'invalid month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]

print(no_of_days(2024,2))