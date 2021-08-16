file_name = input("Enter file name: ")
content = input("Enter content: ")

with open(file_name, 'w') as file:
    file.write(content)

open_file = input("Would you like to open this file? ")
if open_file in ['y', 'n']:
    if open_file == 'y':
        with open(file_name, 'r') as file:
            print(file.read())