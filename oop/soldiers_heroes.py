# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство,
# в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает
# объект типа "герой". У героев есть метод увеличения собственного уровня.
#
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
# Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
#
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с
# более длинным списком, поднимается уровень.
#
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random


class Unit:
    id = 0

    def __init__(self, team):
        Unit.id += 1
        self.id = Unit.id
        self.team = team


class Soldier(Unit):
    def go_after_hero(self, hero):
        print(f'id{self.id}:I go after hero id {hero.id}')


class Hero(Unit):
    level = 1

    def level_up(self):
        self.level += 1
        print(f'id{self.id}: My level is {self.level}')


light = Hero(1)
dark = Hero(2)

first_team, second_team = [], []

for _ in range(int(input('кол-во солдат: '))):
    team = random.randint(1, 2)
    if team - 1:  # 1 - True, 0 - False
        second_team.append(Soldier(team))
    else:
        first_team.append(Soldier(team))

print(f'The team №1 has {len(first_team)} soldiers')
print(f'The team №2 has {len(second_team)} soldiers')

if len(first_team) > len(second_team):
    light.level_up()
elif len(second_team) > len(first_team):
    dark.level_up()

random.choice(first_team).go_after_hero(light)