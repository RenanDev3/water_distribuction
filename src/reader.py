import os


# Verify if the path exists
# needs an argument => the path where the file is
# return a boolean, true if the file is found
def validate_path(path):
    return True if os.path.exists(path) else False


# remove invalid or unnecessary caracters of a string
# needs an argument => string.
# return the string cleaned
def clean_str(str_line):
    return str_line[:-1] if '\n' in str_line else str_line


# generate a list with the data obtained from the csv file
# needs an argument, the path where the file is
# return a list of lists, where each list element is has the row data from the csv file
def generate_list(path):
    with open(path, "r", encoding='utf-8') as file_data:
        return [clean_str(line).split(",") for line in file_data if len(line) > 2]


# Use this functionto get the data
#
# get the list of data from an especific csv file
# needs an argument => one the name of the file : 'meditions'
# return a list of lists where each list element is has the row data from the csv file
def get_list_data(name_file):
    path = f'files_data/{name_file}.csv'
    return generate_list(path=path) if validate_path(path=path) else "File Not Found"

# Use that function