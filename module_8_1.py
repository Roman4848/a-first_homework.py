def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return '{:.3f}{}'.format(a + b, '' if isinstance(b, int) else b)
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return '{:.3f}{}'.format(a, b)
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return '{}{}'.format(a, '{:.0f}'.format(b))
        else:
            raise TypeError("Оба аргумента должны быть либо числами, либо строками")
    except TypeError as e:
        return str(e)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
