"""
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
одинаковое значение некоторой характеристики, и возвращает True, если это так. 
Если значение характеристики для разных объектов отличается - то False.
Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic -
это функция, которая принимает объект и вычисляет его характеристику.
Пример 1:
Ввод:           values [0, 2, 10, 6]
                if same_by(lambda x: x % 2, values):
                    print("some')
                else:
                    print('different')

Вывод:          same

Пример 2:
Ввод:           values = [1, 2, 3, 4]      
                if same_by(lambda x: x % 2, values):
                    print('some')
                else:
                    print('different')

Вывод:          different
"""


def same_by(characteristic, objects):
    some_list = list(filter(characteristic, objects))
    return len(some_list) == len(objects) or len(some_list) == 0


values = [1, 2, 3, 4]
print((same_by(lambda x: x % 2, values)))  # False


values = [0, 2, 10, 6]
print((same_by(lambda x: x % 2, values)))  # True


# ----------------------------------------------------------

"""
Вам уже приходилось писать таблицу умножения. Но на этот раз вас попросили сделать в
плюс к таблице умножения ещё и таблицу сложения, а также таблицу возведения в степень.
Чтобы не копировать один и тот же код и обобщить все три функции до единой функции
рисования таблиц (бинарных) арифметических операций, напишите функцию
print_operation_table(operation, num_rows=9, num_columns=9), которая принимает
в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы.
которые должны быть распечатаны. Нумерация строк и столбцов идёт с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно двааргумента, как, например, у операции умножения.
"""


def print_operation_table(operation, num_rows=9, num_columns=9):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            print(operation(row, col), end='\t')
        print()


print_operation_table(lambda x, y: x * y, 5)
