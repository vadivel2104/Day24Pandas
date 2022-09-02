import pandas as pd

data_file = pd.read_csv("squirrel_census.csv")

set_color = data_file["Primary Fur Color"].to_list()

unique_color = set(set_color)

count = []
fur_color = []

for color in unique_color:
    count.append(len(data_file[data_file["Primary Fur Color"] == color]))
    fur_color.append(color)

dict_color = {"fur": fur_color, "population": count}
dict_color["fur"].pop(0)
dict_color["population"].pop(0)


df = pd.DataFrame(dict_color)
print(df)

