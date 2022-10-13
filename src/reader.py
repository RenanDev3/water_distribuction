import os

#need an argument [name_of_csv_file]
#return a [list_of_dictionaries]
def get_list_of_dictionaries(str_name_file):
    path = f'files_data/{str_name_file}.csv'
    new_list = []
    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as file_data:
            for line in file_data:
                new_list.append(line.split("|"))

    return generate_list_of_dictionaries(new_list[0],new_list[1:])


def generate_dictionay(header, data):
    new_dict={}
    for index in range(len(data)):
        new_dict[header[index]]=data[index]
    return new_dict    


def generate_list_of_dictionaries(headers_list,data_list):
    list_dictionaries = []
    for data in data_list:
        new_dict=generate_dictionay(headers_list,data)
        list_dictionaries.append(new_dict)    

    return list_dictionaries