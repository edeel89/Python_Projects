import pandas

data = pandas.read_csv("Squirrel_Data.csv")
print(data.value_counts("Primary Fur Color"))
