#this will create file, if applicable
with open('example2_text.txt', 'w') as file:
    file.write("Testing 1, 2, 3. Test?")

#append
with open('example2_text.txt', 'a') as file:
    file.write("\nAnother line.")