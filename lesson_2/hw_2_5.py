'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна
отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули,
если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих
товаров по возрастанию, написав минимум кода?

'''

price_list = [57.8, 46.51, 97, 38.9, 47.83, 12, 165.3, 600, 24.94, 66.3]
counter = 0
out_string = ''
out_string_2 = ''

for price in price_list:
    new_price = int(price * 100)
    if str(new_price)[-1] == '0' and type(price) is float:
        price = float(str(price)[0:-1]+'0'+str(price)[-1:])
        price_list[counter] = float(price)
    counter += 1
    if type(price) is float:
        out_string += f'{str(price)[0:-3]} рублей {str(price)[-2:]} коп, '
    else:
        out_string += f'{price} рублей, '

print(out_string[:-2], '\n')


print(id(price_list))  # здесь сортируем список и показываем,
price_list.sort()      # что индексы у списка до и после сортировки идентичны
print(price_list, id(price_list))

sotr_price_list = price_list[::-1]  # здесь список по убыванию
print(sotr_price_list, '\n')

for some_price in sotr_price_list[0:5]:  # выводим 5 самый дорогих
    out_string_2 += f'{some_price}, '

print(out_string_2[:-2])
