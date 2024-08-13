immutable_var = (5, 6.5, "Привет", True, None, [15, 23, 38], {"a": 1, "b": 2})
print(immutable_var)
immutable_var[6][0] = 'rfg'
print(immutable_var)
immutable_var[5][0] = 10l
print(immutable_var)
try:
    immutable_var[0] = 10
except TypeError as e:
    print("\nОшибка при попытке изменить элемент кортежа:")
    print(e)
print("\nКортежи в Python являются неизменяемыми, то есть их элементы нельзя изменить после создания.")
print("Это связано с тем, что кортежи реализованы как неизменяемые объекты в памяти.")
print("Когда вы пытаетесь изменить элемент кортежа, Python выдает ошибку TypeError.")
print("\nОднако, если кортеж содержит изменяемые объекты, такие как списки или словари, то эти объекты можно изменить.")
immutable_var[5][0] = 10
print("Измененный список внутри кортежа:")
print(immutable_var[5])
print("\nОднако, если кортеж содержит изменяемые объекты, такие как списки или словари, то эти объекты можно изменить.")
immutable_var[6]["a"] = 10
print("Измененный словарь внутри кортежа:")
print(immutable_var[6])

mutable_list = ["банан", "какос", 1, 2]
print(mutable_list)
mutable_list[3] = 9
print(mutable_list)
mutable_list[0] = 'шаурма'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend(['Привет', 48])
print(mutable_list)
mutable_list.remove("какос")
print(mutable_list)
print('Привет' in mutable_list)
print('KOK' in mutable_list)
