from abc import ABCMeta, abstractmethod


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def do_weapon(self):
        pass


class Sword(Weapon):
    @abstractmethod
    def do_weapon(self):
        pass


class Bow(Weapon):
    @abstractmethod
    def do_weapon(self):
        pass


class SimpleSword(Sword):
    def do_weapon(self):
        return 10


class UniqueSword(Sword):
    def do_weapon(self):
        return 20


class SimpleBow(Bow):
    def do_weapon(self):
        return 12


class UniqueBow(Bow):
    def do_weapon(self):
        return 24


class WeaponFactory:
    def __init__(self, weapon):
        self.weapon = weapon

    def make_weapon(self):
        return eval(self.weapon)().do_weapon()


if __name__ == "__main__":
    x = WeaponFactory("UniqueBow")
    attack = x.make_weapon()
    print(attack)

