'''
*(вместо задачи 3) Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
'''


def thesaurus_adv(*args):
    emp_inf_dict = {}
    args = list(map(lambda fio: fio.split(' '), args))
    for emp_inf in args:
        if emp_inf[1][0] not in emp_inf_dict.keys():
            emp_inf_dict[emp_inf[1][0]] = {emp_inf[0][0]: emp_inf}
            x = emp_inf_dict[emp_inf[1][0]]
        elif emp_inf[0][0] not in emp_inf_dict[emp_inf[1][0]].keys():
            emp_inf_dict[emp_inf[1][0]][emp_inf[0][0]] = emp_inf
        else:
            emp_inf_dict[emp_inf[1][0]][emp_inf[0][0]].append(emp_inf)

    return emp_inf_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева"))
