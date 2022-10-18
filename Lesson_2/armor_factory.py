from abc import ABCMeta, abstractmethod


class Armor(metaclass=ABCMeta):
    @abstractmethod
    def do_armor(self):
        pass


class LightArmor(Armor):
    @abstractmethod
    def do_armor(self):
        pass


class HardArmor(Armor):
    @abstractmethod
    def do_armor(self):
        pass


class SimpleLightArmor(LightArmor):
    def do_armor(self):
        return 20


class UniqueLightArmor(LightArmor):
    def do_armor(self):
        return 30


class SimpleHardArmor(HardArmor):
    def do_armor(self):
        return 30


class UniqueHardArmor(HardArmor):
    def do_armor(self):
        return 50


class ArmorFactory:
    def __init__(self, armor):
        self.armor = armor

    def make_armor(self):
        return eval(self.armor)().do_armor()


if __name__ == "__main__":
    x = ArmorFactory("SimpleHardArmor")
    defend = x.make_armor()
    print(defend)
