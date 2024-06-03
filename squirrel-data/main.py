import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cin_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cin_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




