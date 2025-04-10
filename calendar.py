from datetime import datetime, timedelta

def generate_month(year, month):
    first_day = datetime(year, month, 1)
    for i in range(31):
        day = first_day + timedelta(days=i)
        if day.month != month:
            break
        print(day.strftime("%A, %B %d, %Y"))


generate_month(2025, 4)