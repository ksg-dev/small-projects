import datetime as dt

now = dt.datetime.now()

# access elements of datetime object
year = now.year
month = now.month
dow = now.weekday()

print(year)

# create your own datetime object - year month day required
my_birthday = dt.datetime(year=2001, month=7, day=5)
print(my_birthday)