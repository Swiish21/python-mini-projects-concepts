dict1 = {
    'value': 11
}

dict2 = dict1

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))

#making changes to dict2

dict2['value'] = 22

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))

#for pointers in dictionary, its different compared to when used with variables,
#changing the value for dict2 directly changes the value of dict1 to match itself.