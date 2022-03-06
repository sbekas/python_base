number_str = input('Введите целое положительное число: ')
number = int(number_str)
max_digit = 0

while number >= 10:
    curr_digit = int(number % 10)
    div = number / 10
    if curr_digit > max_digit:
        max_digit = curr_digit
    number = div
curr_digit = int(div)
if curr_digit > max_digit:
   max_digit = curr_digit

print(f'Наибольшая цифра в числе {number_str} - это {max_digit}')
