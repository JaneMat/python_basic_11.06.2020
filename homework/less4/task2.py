'''Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.'''

my_list = [15, 3, 17, 25, 18, 44, 232, 576]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)