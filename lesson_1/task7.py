"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class TaskBoard():
    def __init__(self, *bases_task):
        self.bases_task = list(bases_task)
        self.resolved_tasks = []
        self.rework = []

    def print_all_task(self):
        print(f'Основные задания {self.bases_task}\n'
              f'Выполненные задания {self.resolved_tasks}\n'
              f'Задания на корректировку {self.rework}\n')

    def add_task(self, el):
        self.bases_task.insert(0, el)

    def finished(self):
        self.resolved_tasks.append(self.bases_task.pop())

    def add_rework_queue(self):
        self.rework.insert(0, self.bases_task.pop())


obj = TaskBoard('сделать дз', 'сходить в магазин', 'приготовить поесть')

obj.print_all_task()
obj.add_task('eating')
obj.finished()
obj.add_rework_queue()
obj.print_all_task()
