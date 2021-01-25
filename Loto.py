import random


def gen(inter):
    return [el for el in range(1, inter)]   # Генератор чисел


class Card:
    # Создаем list с числами, которые будут отображаться на карточке

    def __init__(self):
        self.gen = gen(40)  # Диапазон чисел для генерации
        self.list_game = []
        for idx in range(0, 3):
            chek = []
            for el in range(0, 5):
                chek.append(self.gen.pop(random.randint(0, len(self.gen) - 1)))
                chek.sort()
            for zero in range(0, 4):
                chek.insert(random.randint(0, len(chek) - 1), 0)
            for el in chek:
                self.list_game.append(el)

    # Настраиваем визуализацию карточек

    def __str__(self):
        bounder = '-----------------------'
        ret = bounder + '\n'
        for index, ind in enumerate(self.list_game):
            if int(ind) == 0:
                ret += '  '
            elif ind == -1:
                ret += ' - '
            else:
                ret += str(ind) + ' '
            if (index + 1) % 9 == 0:
                ret += '\n'
        return ret + bounder

    # Далее идут методы для проверки числа на его начилие в карточке

    def __contains__(self, item):
        return item in self.list_game

    def cross_num(self, num):
        for ind, el in enumerate(self.list_game):
            if num == el:
                self.list_game[ind] = -1

    def chek(self) -> bool:
        return set(self.list_game) == {0, -1}


class Game:
    def __init__(self, name) -> int:
        self.name = name
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = gen(40)  # List с кеглями (бочонками)

    def get_keg(self):

        keg = self.__kegs.pop(random.randint(0, len(self.__kegs) - 1))
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'- {self.name}, ваша карточка -\n{self.__usercard}')
        print(f'- Карточка компьютера -\n{self.__compcard}')
        useranswer = input('Зачеркнуть цифру? (y/n) ').lower().strip()

        # Далее идут итоговые проверки, влиящие на ход игры: продолжится она или закончится победой компьютера.

        if keg in self.__usercard and useranswer != 'y' or \
                not keg in self.__usercard and useranswer == 'y':
            return 2

        if keg in self.__usercard and useranswer == 'y':
            self.__usercard.cross_num(keg)
            if self.__usercard.chek():
                return 1

        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.chek():
                return 2


print('Лото!!!\nПобеждает тот, у кого не останется цифр на карточке. Если вы допускаете ошибку - вы проигрываете!')
game = Game(input('Введите имя: ').capitalize())
while True:
    score = game.get_keg()
    if score == 1:
        print(f'{game.name}, ты все-таки победил! Даже если ничья :) ')
        break
    elif score == 2:
        print(f'Очень жаль,{game.name}, но машина победила!')
        break
