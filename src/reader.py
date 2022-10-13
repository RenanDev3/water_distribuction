import os

#need an argument [name_of_csv_file]
#return a [list_of_dictionaries]
def get_list_of_dictionaries(str_name_file):
    path = f'./{str_name_file}.csv'
    new_list = []
    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as file_data:
            for line in file_data:
                new_list.append(line.split("|"))

    return generate_list_of_dictionaries(new_list[0],new_list[1:])

def generate_list_of_dictionaries(headers_list,data_list):
    list_dictionaries = []
    ignored_pos = 1

    for position_a in range(len(data_list)):
        new_dict={}
        for position_b  in range(len(headers_list[0])):
            new_dict[headers_list[0][position_b]]=data_list[position_a][position_b]
        list_dictionaries.append(new_dict)    

    return list_dictionaries