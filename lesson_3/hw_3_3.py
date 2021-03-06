'''
Написать функцию thesaurus(),
принимающую в качестве аргументов имена сотрудников и
возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
'''


def thesaurus(*args):
    names_dict = {}
    for name in args:
        if name[0] not in names_dict.keys():
            names_dict[name[0]] = [name]
        else:
            names_dict[name[0]].append(name)
    return names_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Галина", "Anonymous"))
