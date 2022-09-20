# Days In Month
year = int(input("Year:\n"))
month = int(input("Month:\n"))

# Check Leap or not a leap year
def leap_year(year_check):
    """Check if year is leap"""
    if year_check % 4 == 0:
        if year_check % 100 == 0:
            if year_check % 400 == 0:
                return  True
            else:
                return  False
        else:
            return  True 
    else:
        return  False

# count days in a month
def days_in_month(check_year, month_is):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    if leap_year(check_year):
        days_in_month[1] = 29
        days = days_in_month[month_is - 1]
    else:
        days = days_in_month[month_is - 1]
    return f"Total days in month {month_is} are {days}."

print(days_in_month(year, month))
