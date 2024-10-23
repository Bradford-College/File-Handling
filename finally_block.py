try:
    # Attempt to open the file in read mode
    file = open('example.txt', 'r')
    # Read the contents of the file
    data = file.read()
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("File not found!")
finally:
    # Ensure the file is closed, whether or not an exception occurred
    file.close()
