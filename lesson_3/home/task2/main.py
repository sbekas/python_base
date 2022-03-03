# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def user_bio(name='', surname='', birth_year='', location='', email='', phone=''):
    result = f'Имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город проживания: {location}, email: {email}, телефон: {phone}'
    return result


my_name = input('Введите имя: ')
my_family = input('Введите фамилию: ')
city = input('Введите город проживания: ')
birth = input('Введите год рождения: ')
my_email = input('Введите ваш email: ')
phone_num = input('Введите ваш номер телефона')

bio_str = user_bio(phone=phone_num, surname=my_family, name=my_name, birth_year=birth, location=city)
print(bio_str)
