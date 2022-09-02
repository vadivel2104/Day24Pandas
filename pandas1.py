import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# avg = sum(temp_list)/(len(temp_list)+1)
#
# print(avg)
#
# print(round(data["temp"].mean(), 2))

print(data[data.temp == (data["temp"].max())])

# print(data[data.temp == max_temp])