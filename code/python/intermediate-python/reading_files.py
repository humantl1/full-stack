#simplified syntax, but still uses abbreviations and keywords
#scope for file is contained within open block
#so the stream is closed when the scope is exited

#'r' denotes 'read', 'file' is variable name
with open('example_text.txt', 'r') as file:
    #content = file.read() #store file in variable
    print(file.readline())
    print(file.read()) #takes an argument specifying # of characters returned
    i = 7
#output:
#This is file text
# (blank line)
#and this is the next line of text
#So this makes it seem that readline reads to the end of a line BUT not the
#carriage return. And the position of the reader is stable within the scope

print(i)
#print("stored content: ", content) #how is content accessed outside of scope?
