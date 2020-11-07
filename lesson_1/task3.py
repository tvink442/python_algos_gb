"""
Задание 3.
Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
res = {'a': 3, 'x': 7, 's': 6, 'h': 20, 'n': 11}

# 1 O(n) Чем меньше кода тем лучше, и так как линейная скорость то этот вариант лучше
for i in res:
    if res[i] in sorted(res.values())[-3:]:
        print(f'{i} : {res[i]}')


# 2 O(n**2)
count = 3
res_copy = res.copy()
while count:
    for i in res_copy:
        if res_copy[i] == max(res_copy.values()):
            print(f'{i} : {res_copy.pop(i)}')
            break
    count -= 1

