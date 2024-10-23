'''
Assignment:

1. Read content from a text file named 'input.txt'.
2. Convert the content to a dictionary format.
3. Write the dictionary data to a JSON file named 'output.json'.
4. Implement exception handling to manage potential errors such as file not found or read/write errors.
'''
import json

# Step 1: Reading from a text file
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Text File Content:")
            print(content)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Writing data to a JSON file
def write_json_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
            print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Reading from a text file
    read_text_file('example.txt')

    # Data to write to JSON
    sample_data = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }

    # Writing to a JSON file
    write_json_file(sample_data, 'data.json')