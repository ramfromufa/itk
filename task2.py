class CycleList:

    def __init__(self, item_list):
        self.item_list = item_list
        self.current_i = 0
        self.length = len(item_list)

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.item_list)
 
    def __getitem__(self, i):
        i = i % self.length
        return self.item_list[i]

    def __iter__(self):
        return self

# По названию класса я решил сделать его бесконечным и для функции next().
# Я экспериментировал.
# Как оказалось цикл "for i in cl:" работает и с __getitem__, и с __next__
# Приоритетно со вторым. Возникает вопрос, что будет быстрей или лучше?

    def __next__(self):
        if self.current_i < self.length:
            val = self.current_i
            self.current_i += 1
            return self.item_list[val]
        else:
            self.current_i = 1
            return self.item_list[0]
