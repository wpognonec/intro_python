my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_integers(int_list):
#     new_list = []
#     for element in int_list:
#         if type(element) == int:
#             new_list.append(element)
#     return new_list

def find_integers(int_list):
    return [ element for element in int_list if type(element) == int ]


integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
