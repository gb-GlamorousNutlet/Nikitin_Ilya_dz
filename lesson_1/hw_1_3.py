for num in range(1, 101):
    if 5 <= num <= 20:
        print(f'{num} процентов')
    elif str(num)[-1] == '1':
        print(f'{num} процент')
    elif 2 <= int(str(num)[-1]) <= 4:
        print(f'{num} процента')
    elif int(str(num)[-1]) == 0 or 5 <= int(str(num)[-1]) <= 9:
        print(f'{num} процентов')
