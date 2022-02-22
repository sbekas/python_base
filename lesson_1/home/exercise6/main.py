a_str = input('Введите количество км в первый день, а = ')
b_str = input('Введите значение цели, b = ')
day = 1
print(f'{day}-й день: {a_str}')
a = float(a_str)
b = float(b_str)
while b > a:
    a *= 1.1
    day += 1
    print(f'{day}-й день: {a:.2f}')
print(f'На {day}-й день спортсмен достиг результата - не менее {b_str} км')
