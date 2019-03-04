# Dictionary
# the clear method

# dictionary.clear()
print('Clear method')
phonebook = {'Chris' : '555-1111', 'Katie' : '555-222'}
print(phonebook)

phonebook.clear()
print(phonebook)

# the get method
# dictionary.get(key, default)
print('Get method')
phonebook = {'Chris' : '555-1111', 'Katie' : '555-222'}
value = phonebook.get('Katie', 'Entry not found')
print(value)
value = phonebook.get('Andy', 'Entry not found')
print(value)

# the items method
# dictionary.items()
print('Items method')
phonebook = {'Chris' : '555-1111', 'Katie' : '555-222'}
items = phonebook.items()
print(items)

# the keys method
# dictionary.keys()
print('The keys method')
phonebook = {'Chris':'555-1111', 'Katie':'555-222'}
keys = phonebook.keys()
print(keys)

