my_dict = {'Roman': 1995}
print(my_dict)
print(my_dict['Roman'])
my_dict.update({'Valera': 1993,
                'Maha': 1994})
del my_dict['Valera']
print(my_dict.get('Valera', 'Такого ключа нету'))
print(my_dict)

my_set = {1, 2, 2, 3, 1, 3, "привет", "привет", 4.5, True, False, True}
print(my_set)
my_set.add("кокос")
my_set.add(6)
my_set.remove(2)
print(my_set)