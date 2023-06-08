f = open("./Input/Letters/starting_letter.txt")
contents = f.read()
l = open("./Input/Names/invited_names.txt")

for line in l:
    a = line.replace("\n", "")
    x = contents.replace("[name]", a)
    new_file = open(f"./Output/ReadyToSend/{a}.txt", "w")
    new_file.write(x)
    
new_file.close()
f.close()
l.close()

#with open("./Output/adeel.txt", mode="w") as file2:
    #file2.write(x)
