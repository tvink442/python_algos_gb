"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def res(lst, even='', uneven=''):
    if len(lst) == 0:
        return f'{len(even)} even number  ({even}) ,' \
               f' {len(uneven)} uneven number  ({uneven})'
    first = lst[:1]
    if int(first) % 2 == 1:
        uneven += first
        return res(lst[1:], even, uneven)
    elif int(first) % 2 == 0:
        even += first
        return res(lst[1:], even, uneven)


print(res(input()))
