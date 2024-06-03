import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# average_temp = data["temp"].mean()
# print(average_temp)

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_c = monday.temp
# monday_f = (monday_c * 1.8) + 32
# print(monday_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pd.DataFrame(data_dict)

# Write df to csv file
data.to_csv("new_data.csv")
print(new_data)