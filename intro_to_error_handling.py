try:
    # Attempt to open a file that does not exist
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print(f'File not found!')
