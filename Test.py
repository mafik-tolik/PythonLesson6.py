import os
import math
import random

os.system('cls')

# -------------------------------------------------------------------------------------------


print('\n3. Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в '
      'строку, сворачивая соседние по числовому ряду числа в диапазоны.\nПримеры:\n[1,4,5,2,3,9,8,11,0] => '
      '"O-5,8-9,11"\n[1,4,3,2] => "1-4"\n[1,4] => "1,4"\nРешение:')

some_list1 = [1, 4, 5, 2, 3, 9, 8, 11, 0]
print(f'{some_list1} => ')
text1 = ''


def minimum(some_list):
    min = some_list[0]
    for i in range(1, len(some_list)):
        if some_list1[i] < min:
            min = some_list1[i]
    return min


while len(some_list1) != 0:

    maxx = some_list1[0]
    minn = minimum(some_list1)

    if len(some_list1) == 1:
        text1 = text1 + str(some_list1[0])
        some_list1.pop(0)
        break
    else:
        text1 = text1 + str(minn) + '-'

        for i in range(0, len(some_list1)-1):
            if some_list1[i] > some_list1[i+1]:
                maxx = some_list1[i]
                text1 += str(some_list1[i]) + ','
                break

        some_list1 = list(filter(lambda i: i > maxx, some_list1))
        if len(some_list1) == 0:
            text1 = text1[:-1]

print(text1)
