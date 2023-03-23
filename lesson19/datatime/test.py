from datetime import datetime, timedelta

current_datetime = datetime.now()
print(current_datetime)

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)


print(current_datetime.date())
print(current_datetime.time())

d1 = datetime(year=2022, month=7, day=14)
print(d1.weekday())

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday())

# current_datetime = datetime.now()
# next_month = datetime.now()
# year = next_month.month + 1  # next_month.month
# next_month.year = year
# print(current_datetime < next_month)

seventh_day_2021 = datetime(year=2021, month=1, day=7, hour=14)
seventh_day_2022 = datetime(year=2022, month=1, day=7, hour=14)

difference = seventh_day_2022 - seventh_day_2021
print(difference.days)
print(difference.total_seconds())

four_weeks_interval = timedelta(weeks=4)
print((seventh_day_2022 + four_weeks_interval).date())
print((seventh_day_2022 - four_weeks_interval).date())


delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=10,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

ts = seventh_day_2020.timestamp()
print(ts)

ts += 100_000_0000
print(datetime.fromtimestamp(ts))

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.strftime('%A %d %B %Y'))

date_of_birth = datetime(year=2004, month=11, day=28)
print((datetime.now() - date_of_birth).days / 30 / 12)

s = '28 November 2004'
print(s)
print((datetime.now() - datetime.strptime(s, '%d %B %Y')).days / 30 / 12)
