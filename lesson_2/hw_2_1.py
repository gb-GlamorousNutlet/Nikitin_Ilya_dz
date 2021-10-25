'''
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
'''

expression_1, expression_2 = 15 // 2, 15 ** 2
expression_3, expression_4 = 15 * 3, 15 / 3
print(type(expression_1), type(expression_2),
      type(expression_3), type(expression_4))
