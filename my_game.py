import random


class Unit:
    _random_chance = 0

    def __init__(self, name='unnamed_unit', health=100, attack=0, defence=0):
        self._name_of_unit = name
        self._health_of_unit = health
        self._attack_level = attack
        self._defence_level = defence

    @property
    def name(self):
        return self._name_of_unit

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name_of_unit = name
        else:
            print("It should be a string")

    @property
    def health(self):
        return self._health_of_unit

    @health.setter
    def health(self, health):
        if isinstance(health, int):
            self._health_of_unit = health
        else:
            print("It should be an integer")

    @property
    def attack(self):
        return self._attack_level

    @attack.setter
    def attack(self, attack):
        if isinstance(attack, int):
            self._attack_level = attack
        else:
            print("It should be an integer")

    @property
    def defence(self):
        return self._defence_level

    @defence.setter
    def defence(self, defence):
        if isinstance(defence, int):
            self._defence_level = defence
        else:
            print("It should be an integer")

    def hit(self, unit):
        whole_unit_life = unit.health + unit.defence
        if whole_unit_life <= self.attack:
            unit.health = 0
        else:
            if unit.defence >= self.attack:
                unit.defence = unit.defence - self.attack
            else:
                unit.defence = 0
                unit.health = unit.health - (self.attack - unit.defence)


class Knight(Unit):
    _random_chance = 0.3

    def hit(self, unit):
        modified_attack = self.attack
        if random.random() < self._random_chance:
            modified_attack = self.attack * 2
        whole_unit_life = unit.health + unit.defence
        if whole_unit_life <= modified_attack:
            unit.health = 0
            unit.defence = 0
        else:
            if unit.defence >= modified_attack:
                unit.defence -= modified_attack
            else:
                unit.defence = 0
                unit.health -= (modified_attack - unit.defence)


class Brigand(Unit):
    _random_chance = 0.15

    @property
    def defence(self):
        return self._defence_level

    @defence.setter
    def defence(self, defence):
        if isinstance(defence, int):
            if random.random() > self._random_chance:
                self._defence_level = defence
            else:
                pass
        else:
            print("It should be an integer")

    @property
    def health(self):
        return self._health_of_unit

    @health.setter
    def health(self, health):
        if isinstance(health, int):
            if random.random() > self._random_chance:
                self._health_of_unit = health
            else:
                pass
        else:
            print("It should be an integer")


class Mage(Unit):
    _random_chance = 0.05


# test data

def test_data_1():

    k1 = Knight(name='Knight_1', health=100, attack=25, defence=0)
    print(k1.__dict__)
    k2 = Knight(name='K_2', health=100, attack=10, defence=100)
    print(k2.__dict__)
    k1.hit(k2)
    print(k2.__dict__)
    k1.hit(k2)
    print(k2.__dict__)
    k1.hit(k2)
    print(k2.__dict__)
    k1.hit(k2)
    print(k2.__dict__)


# test_data_1()



def test_data_2():

    k1 = Knight(name='Knight_1', health=100, attack=20, defence=0)
    print(k1.__dict__)
    print(dir(k1))

    b2 = Brigand(name='Brigand_2', health=100, attack=0, defence=100)
    print(b2.__dict__)
    print(dir(k1))

    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)
    k1.hit(b2)
    print(b2.__dict__)

# test_data_2()
