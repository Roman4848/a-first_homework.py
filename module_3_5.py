def get_multiplied_digit(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digit(int(str_number[1:]))
    else:
        return int(str_number)
result = get_multiplied_digit(40203)
print(result)