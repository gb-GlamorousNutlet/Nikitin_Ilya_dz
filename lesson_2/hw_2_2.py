'''
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура',
'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число
(вещественные не трогаем) кавычками (добавить кавычку до и
кавычку после элемента списка, являющегося числом) и
дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками
не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
'''

some_list = ['в', '5', 'часов', '17', 'минут',
             'температура', 'воздуха', 'была', '+5', 'градусов']
new_some_list = []

for exp in some_list:
    if ord(exp[0]) in range(49, 57) and int(exp) // 10 < 1:
        new_some_list.append(f'"0{exp}"')
    elif exp[0] == '+' and int(exp[1:]) // 10 < 1:
        new_some_list.append(f'"{exp[0]}0{exp[1:]}"')
    elif ord(exp[0]) in range(49, 57):
        new_some_list.append(f'"{exp}"')
    else:
        new_some_list.append(exp)


print(' '.join(new_some_list))
