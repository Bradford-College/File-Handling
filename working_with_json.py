import json  # Import the JSON module

# Create a dictionary with some data
data = {"name": "Alice", "age": 25}

# Open a file named 'data.json' in write mode
with open('data.json', 'w') as file:
    # Write the dictionary to the file in JSON format
    json.dump(data, file, indent = 4)