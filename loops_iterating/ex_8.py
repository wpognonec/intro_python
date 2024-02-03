my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = {
    key: len(key)
    for key in my_set
    if len(key) % 2 != 0
}

print(new_dict)