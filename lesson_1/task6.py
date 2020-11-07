"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackOfPlates:
    def __init__(self):
        self.elems = [] # основной стек
        self.temp = [] # временный
        self.max_stack = 6

    def get_count(self):
        print(self.elems)
        print(self.temp)

    #при заполнении временного стека, он добавляется в основной
    # а временный обнулется
    def push_in(self):
        if len(self.temp) != self.max_stack:
            self.temp.append('plate')
        elif len(self.temp) == self.max_stack:
            self.elems.append(self.temp[:])
            self.temp.clear()

    def pop_out(self):
        if len(self.temp):
            return self.temp.pop()
        return self.elems[-1].pop()

    def count_stacks(self):
        if self.temp:
            count = 1
        return len(self.elems) + count


obj = StackOfPlates()

for i in range(18):
    obj.push_in()
obj.get_count()
print(obj.count_stacks())
for i in range(10):
    print(obj.pop_out())
    obj.get_count()
obj.get_count()