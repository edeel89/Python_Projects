import pandas

my_dict = {}
my_list = []
data = pandas.read_csv("alphabet.csv")
for (index, row) in data.iterrows():
    my_dict[row.letter] = row.code
name = input("Enter your name: ")
name = name.upper()
for i in name:
    my_list.append(my_dict[i])
print(my_list)
