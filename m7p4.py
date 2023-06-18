#Luan Nguyen

#June 8th 2023

#
def my_function(my_list):
    number_list =[]
    for i in my_list:
        if i not in number_list:
            number_list.append(i)
    return number_list

my_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(my_function(my_list))
