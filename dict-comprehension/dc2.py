# TODO use DC to create dict weather_f that takes
#  day of week as key and temp as value in C and converts to F
# Example input: {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14,
# "Friday": 21, "Saturday": 22, "Sunday": 24}
# eval used to read input as dict
weather_c = eval(input())

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
