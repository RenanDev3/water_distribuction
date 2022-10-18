from reader import get_list_data

# needs an argument => string date ''dd/mm/yyyy' for 'date_lecture'
# return a list that containts list of lists that has the same date [id,code_meter,initial_lecture,last_lecture,date_lecture,first_meter_lecture] 
def get_list_data_by_date(str_date):
    data = get_list_data('meditions')
    position = data[0].index('date_lecture')
    filtered_list = filter(lambda list_element: (list_element[position] == str_date), data)
    return list(filtered_list)

# It should be deleted
# example
info_per_date = get_list_data_by_date('06/09/2022')

# It should be deleted
# It will show the elements contained int the list [info_per_date]
[print(element) for element in info_per_date]