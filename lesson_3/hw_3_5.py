'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или
запрещающий повторы слов в шутках (когда каждое слово можно использовать
только в одной шутке)? Сможете ли вы сделать аргументы именованными?

'''
from random import choice


def get_jokes(jokes_count, repeat=True):
    """

    Функция генерирует шутки, выбирая случайные значения из 3-ех списков.

    Параметры:
    - jokes_count - количество шуток, которые программа попытается создать.
    - repeat (по умолчанию True). Если стоит False, функция будет использовать
    только уникальные значения

    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if repeat is True:
        for i in range(jokes_count):
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        nouns = {i: j for i, j in enumerate(nouns)}
        adverbs = {i: j for i, j in enumerate(adverbs)}
        adjectives = {i: j for i, j in enumerate(adjectives)}
        for i in range(jokes_count):
            x, y, k = (choice(list(nouns.keys())),
                       choice(list(adverbs.keys())),
                       choice(list(adjectives.keys())))
            print(f'{nouns[x]} {adverbs[y]} {adjectives[k]}')
            nouns.pop(x)
            adverbs.pop(y)
            adjectives.pop(k)
            if len(nouns) == 0:
                print(f'\nШуток больше нет, слова закончились')
                break

get_jokes(2)
print('\n')
get_jokes(20, repeat=False)
