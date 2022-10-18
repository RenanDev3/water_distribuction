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



    
















# def generate_list(path):
#     data_list = []
#     with open(path, "r", encoding='utf-8') as file_data:
#         # for line in file_data:
#         #     data_list.append(clean_str(line).split(","))
#         data_list = [clean_str(line).split(",") for line in file_data if len(line) > 0]

#     return data_list[1:]



# def validate_path(path):
#     # name_file = 'meditions'
#     # path = f'files_data/{name_file}.csv'
#     return True if os.path.exists(path) else False





# def get_list_data():
#     data_list = []
#     path = f'files_data/meditions.csv'

#     if validate_path== False:
#         return "File doesn't exist"

#     with open(path, "r", encoding='utf-8') as file_data:
#         for line in file_data:
#             data_list.append(clean_str(line).split(","))
    
#     return data_list[1:]









# def get_list_of_dictionaries(str_name_file):
#     str_file = 'meditions'
#     path = f'files_data/{str_file}.csv'
#     new_list = []
#     if os.path.exists(path):
#         with open(path, "r", encoding='utf-8') as file_data:
#             for line in file_data:
#                 new_list.append(line.split("|"))

#     return generate_list_of_dictionaries(new_list[0],new_list[1:])


# def generate_dictionay(header_list, data_list):
#     new_dict={}
#     for index in range(len(data_list)):
#         new_dict[header_list[index]]=data_list[index]
#     return new_dict    


# def generate_list_of_dictionaries(headers_list,data_list):
#     list_dictionaries = []
#     for data in data_list:
#         new_dict=generate_dictionay(headers_list,data)
#         list_dictionaries.append(new_dict)    

#     return list_dictionaries



# import re
# from reader import get_list_of_dictionaries
# # a function that returns True if letter is vowel
# def filter_movies_by_rating(rating_input):
#     list_ratings = get_list_of_dictionaries("ratings")
#     list_ratings_filtered = filter(lambda dictionary: (dictionary["rating"] == rating_input), list_ratings)
#     new_list = []
#     for element in list_ratings_filtered:
#       new_list.append(element["movieId"])

#     return list(set(new_list))


# def get_movies_by_rating(rating):
#     new_list = []
#     list_ids_movies = filter_movies_by_rating(rating)
#     list_movies = get_list_of_dictionaries("movies")
#     for element in list_movies:
#       new_dic = {}
#       if element["movieId"] in list_ids_movies:
#         new_dic["title"] = element["title"]
#         numbers_date = re.findall('[0-9]+', element["title"])
#         for number in numbers_date:
#           if int(number)>1000:
#             date_re = number
#         new_dic["date_release"] = date_re 
#         new_dic["genres"] = element["genres"]
#         new_dic["rating"] = [rating,"fecha de comentario"]
#         new_list.append(new_dic)

#     return new_list
