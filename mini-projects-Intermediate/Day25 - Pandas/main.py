# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     data_list = []
#     for row in data:
#         if row[0] != 'day':
#             data_list.append(row)
#     print(data_list)


import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].sum())
# print(data[["day", "temp"]])

# print(data.iloc[0])
# print(data.iloc[0:3]  )# rows 0, 1, 2)
#
# print(data[data["temp"] > 20])
# print("aaaaaaaaaaaaaaaaaaaaaaaaa")
# for index, row in data.iterrows():
#     print(row["day"], row["temp"])


# data = data[data["day"] == "Monday"]
# print(data["temp"][0] * 9/5+32)
