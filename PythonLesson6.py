import msvcrt

print('\n5. Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в '
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

msvcrt.getch()
print('\n6. Дана строка (возможно, пустая), состоящая из букв A-Z:\n'
      'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB\n'
      'Нужно написать функцию RLE, которая на выходе даст строку вида:\n'
      'A4B3C2XYZD4E3F3A6B28\nИ сгенерирует ошибку, если на вход пришла невалидная строка.\n'
      'Пояснения:\nЕсли символ встречается 1 раз, он остается без изменений;\n'
      'Если символ повторяется более 1 раза, к нему добавляется количество повторений.'
      '\nРешение:')


stroka1 = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'


def compress(text2):

    ind = 0
    count = 1
    text3 = ''
    dictionary = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                  'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', ' w', 'x', 'y', 'z'}

    for j in text2:
        if j not in dictionary:
            print('На вход пришла невалидная строка')
            return text3

    while ind < len(text2) - 1:
        if text2[ind] == text2[ind + 1]:
            count += 1
            if ind == len(text2) - 2:
                text3 += text2[ind] + str(count)
        else:
            if count == 1:
                text3 += text2[ind]
            else:
                text3 += text2[ind] + str(count)
            if ind == len(text2) - 2:
                text3 += text2[ind + 1]
            count = 1
        ind += 1

    return text3


stroka2 = compress(stroka1)
print(f'Сжатие: {stroka2}')


def decompress(text5):
    count = ''
    text6 = ''
    i = 0
    while i < len(text5)-1:
        if not text5[i].isdigit():
            if not text5[i+1].isdigit():
                text6 += text5[i]
            else:
                j = 1
                while i+j < len(text5) and text5[i+j].isdigit():
                    count += text5[i+j]
                    j += 1
                text6 += int(count) * text5[i]
                count = ''
        i += 1
        if i == len(text5)-1 and not text5[i].isdigit():
            text6 += text5[i]

    return text6


stroka3 = decompress(stroka2)
print(f'Распаковка: {stroka3}')
