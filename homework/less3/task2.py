''' Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
 год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
  Реализовать вывод данных о пользователе одной строкой.'''

name = input('name')
surname = input('surname')
year = int(input('year'))
city = input('city')
email = input('email')
telephone = input('telephone')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name=' Jane', surname=' Mat', year=' 1996', city=' Smr', email=' jane@mail.ru',
              telephone=' 8927'))