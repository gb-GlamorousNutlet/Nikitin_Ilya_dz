'''
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
Например:
num_translate_adv("One")
Один
num_translate_adv("two")
два
'''


def num_translate_adv(en_word):
    en_ru_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if ('A' <= en_word[0] <= 'Z' and
            en_ru_dict.get(en_word.lower()) is not None):
        return en_ru_dict.get(en_word.lower()).capitalize()
    else:
        return en_ru_dict.get(en_word)

print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print(num_translate_adv('eleven'))
print(num_translate_adv('Twelve'))
