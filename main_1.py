result = 9 ** 0.5 * 5
print(result)

result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

without_priority = 2 * 2 + 2
with_priority = 2 * (2 + 2)
comparison_result = without_priority == with_priority
print(without_priority)
print(with_priority)
print(comparison_result)

number_str = '123.456'
number_float = float(number_str)
shifted_number = number_float * 10
integer_part = int(shifted_number)
first_digit_after_dot = integer_part % 10  

print(first_digit_after_dot)