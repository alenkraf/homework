with open("10\examplefile.txt", "w") as new_file:
    new_file.write("Hello file world!")

with open("10\examplefile.txt", "r") as read_file:
    print(read_file.read())