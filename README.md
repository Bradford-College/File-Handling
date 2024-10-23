# File Handling Activity

Welcome to the File Handling Activity! This README will guide you through the various files and their purposes, as well as the steps to complete the class activity.

## Files Overview

### `working_with_json.py`
This script demonstrates how to write a dictionary to a JSON file.
```py
import json

data = {"name": "Alice", "age": 25}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

### `reading_from_json.py`
This script shows how to read data from a JSON file and print it.
```py
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))
```

### `finally_block.py`
This script illustrates the use of a `finally` block to ensure a file is closed after attempting to read it.
```py
try:
    file = open('example.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
```

### `file_open_close.py`
This script demonstrates basic file operations: opening, reading, and closing a file.
```py
file = open('example.txt', 'r')
data = file.readlines()
print(data)
file.close()
```

### `intro_to_error_handling.py`
This script shows basic error handling when attempting to open a non-existent file.
```py
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print('File not found!')
```

### `writing_to_text_files.py`
This script demonstrates how to write text to a file.
```py
file = open('example_2.txt', 'w')
file.write("Hello, World!\nThis is a test.")
file.close()
```

### `example.txt`
This text file contains a short story.
```txt
Once upon a time in a small village nestled between rolling hills, there lived a young girl named Lily...
```

### `example_2.txt`
This text file contains a simple message.
```txt
Hello, World!
This is a test.
```

### `solution_to_class_activity.py`
This script provides solutions to the class activity, including reading from a text file and writing to a JSON file.
```py
import json

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

def write_json_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
            print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_text_file('example.txt')
    sample_data = {"name": "Alice", "age": 25, "city": "New York"}
    write_json_file(sample_data, 'data.json')
```

### `class_activity.py`
This script outlines the assignment for the class activity.
```py
'''
Assignment:

1. Read content from a text file named 'input.txt'.
2. Convert the content to a dictionary format.
3. Write the dictionary data to a JSON file named 'output.json'.
4. Implement exception handling to manage potential errors such as file not found or read/write errors.
'''
```

## Class Activity Steps

1. **Read content from a text file**: Use the `read_text_file` function to read content from `input.txt`.
2. **Convert the content to a dictionary**: Parse the content as needed to create a dictionary.
3. **Write the dictionary to a JSON file**: Use the `write_json_file` function to write the dictionary to `output.json`.
4. **Implement exception handling**: Ensure your code handles potential errors gracefully.

Good luck, and happy coding!