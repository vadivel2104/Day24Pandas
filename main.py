import csv
box = []
with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        box.append(row)

for data in range(1, len(box)-1):
    print(box[data])

# print(box[-4:])