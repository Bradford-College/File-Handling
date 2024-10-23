import json  # Import the JSON module

# Open the JSON file in read mode
with open('data.json', 'r') as file:
    data = json.load(file)  # Read and parse the JSON data from the file

print(json.dumps(data, indent=4))  # Print the parsed JSON data
