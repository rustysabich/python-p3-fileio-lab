def write_file(file_name, file_content):
    # write the content to a .txt file with the names passed
    with open(f'{file_name}.txt', mode='w') as my_file:
        my_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a') as my_file:
        my_file.write(append_content)
        my_file.close()

def read_file(file_name):
    with open(f'{file_name}.txt', mode='r') as my_file:
        return my_file.read()
