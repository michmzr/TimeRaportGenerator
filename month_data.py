from datetime import datetime
from calendar import monthrange

import holidays

pl_holidays = holidays.country_holidays('PL')


def generate_dates_records(year: int, month_nr: int, out_days: []):
    mr = monthrange(year, month_nr)
    first_workday = 1
    last_workday = mr[1]

    records = []
    for day in range(first_workday, last_workday + 1):
        day_date = datetime(year, month_nr, day).date()
        day_mm_yy = day_date.strftime("%d-%m-%Y")

        is_ooo = any([od for od in out_days if od==day_date ])
        holiday = is_holiday(day_date)
        is_workday = day_date.weekday() < 5

        records.append({
            "date": day_date,
            "day": day_mm_yy,
            "ooo": is_ooo,
            "holiday": holiday,
            "workday": (is_workday)
        })

    return records


def is_holiday(date: datetime):
    return date in pl_holidays
