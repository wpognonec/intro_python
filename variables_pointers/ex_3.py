dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1) #creates a shallow copy
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python']) #'The Life of Brian'

