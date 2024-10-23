# Open the file 'example.txt' in read mode ('r')
file = open('example.txt', 'r')  

# Read the entire content of the file
data = file.readlines()

# Print the content of the file to the console
print(data)

# Always close the file to free up system resources
file.close()