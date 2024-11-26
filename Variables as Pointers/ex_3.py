dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': [1, 2],
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])