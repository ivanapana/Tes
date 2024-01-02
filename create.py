# Creating a new file
with open ('ivansondakh.txt', 'r') as file:
    # Writing some code into the file
    #file.write("print('Hello, World!)")
    # reading the content of the file
    content = file.read()

    # Printing the content of the file
    print (content)