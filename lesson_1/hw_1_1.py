sec_count = int(input('Введите кол-во секунд: '))

if 0 <= sec_count < 60:
    print(f'{sec_count} сек')
elif 60 <= sec_count < 3600:
    print(f'{sec_count // 60} мин {sec_count % 60} сек')
elif 3600 <= sec_count < 86400:
    print(f'{sec_count // 3600} час {sec_count % 3600 // 60} мин '
          f'{sec_count % 3600 % 60 % 60} сек')
elif sec_count >= 86400:
    print(f'{sec_count // 86400} дн {sec_count % 86400 // 3600} час '
          f'{sec_count % 86400 % 3600 // 60} мин '
          f'{sec_count % 86400 % 3600 % 60} сек')
else:
    print('Введите корректное значение!')
