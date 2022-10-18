from reader import get_list_data


# needs an argument => ID of user 'user_id'
# return a list that containts the [id,code_meter,user_id,active] 
def get_data_by_user_id(str_id):
    data = get_list_data('water_meters')
    position = data[0].index('user_id')
    filtered_list = filter(lambda list_element: (list_element[position] == str_id), data)
    return list(filtered_list)


# It should be deleted
# example
info_per_date = get_data_by_user_id('123455')

# It should be deleted
# It will show the elements contained int the list [info_per_date]
[print(element) for element in info_per_date]