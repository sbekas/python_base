seconds_str = input('Введите количесвто секунд: ')
seconds = int(seconds_str)
hours = int(seconds / 3600)
ostatok_h = seconds % 3600
minutes = int(ostatok_h / 60)
ostatok_min = ostatok_h % 60
print(f'{seconds} секунд это: {hours:02}:{minutes:02}:{ostatok_min:02}')
#если установить боьшое число, например, 365987,
# интерепретатор игнорирует указанное количество разрядов почему-то
