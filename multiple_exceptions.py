import json

# Try to open and read the JSON file
try:
    file = open('data.json', 'r')
    data = json.load(file)
    print(data)

# Handle the case where the file is not found
except FileNotFoundError:
    print("File not found!")

# Handle the case where the JSON is not properly formatted
except json.JSONDecodeError:
    print("Error decoding JSON!")