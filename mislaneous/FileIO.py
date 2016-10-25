# writing to files
with open("test2.txt",'w') as file:
    for i in range(11):
        file.write(str(i)+"\n")

# reading files
with open("test2.txt") as open_file:
    for line in open_file:
        print(line.strip() + " ", end="")
