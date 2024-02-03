dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) #shallow copy only copies top level items. nested items are the same object id.
dict1['a'][1] = 42
print(dict2['a']) #[1, 42, 3]