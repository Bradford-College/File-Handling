# Open the file 'example_2.txt' in write mode ('w')
# This will create the file if it does not exist, or truncate it if it does
file = open('example_2.txt', 'w')

# Write the string "Hello, World!\nThis is a test." to the file
# \n is a newline character, so "This is a test." will be on a new line
file.write("Hello, World!\nThis is a test.")

# Close the file to ensure all data is written and resources are freed
file.close()