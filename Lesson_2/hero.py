from weapon_factory import Weapon, Sword, Bow, SimpleSword, UniqueSword, SimpleBow, UniqueBow, \
    WeaponFactory
from armor_factory import Armor, LightArmor, HardArmor, SimpleLightArmor, UniqueLightArmor, SimpleHardArmor, \
    UniqueHardArmor, ArmorFactory
from abc import ABCMeta, abstractmethod


class Hero(metaclass=ABCMeta):
    def __init__(self, attack=0, defend=0, health=100):
        self.health = health
        self.attack = attack
        self.defend = defend

    @abstractmethod
    def enemy_attack(self, attack_object):
        pass


class Knight(Hero):
    def enemy_attack(self, attack_object):
        attack_object.health -= (self.attack * (1 - (attack_object.defend / 100)))


class Bower(Hero):
    def enemy_attack(self, attack_object):
        attack_object.health -= (self.attack * (1 - (attack_object.defend / 100)))


if __name__ == "__main__":
    x = WeaponFactory("UniqueSword")
    attack = x.make_weapon()

    y = ArmorFactory("SimpleHardArmor")
    defend = y.make_armor()

    hero1 = Knight(attack, defend)
    hero2 = Bower(10, 50)
    print(hero1.health, '---', hero2.health)
    print(hero1.attack, '---', hero2.attack)
    print(hero1.defend, '---', hero2.defend)

    hero1.enemy_attack(hero2)
    hero2.enemy_attack(hero1)
    print(hero1.health, '---', hero2.health)
    print(hero1.attack, '---', hero2.attack)
    print(hero1.defend, '---', hero2.defend)

    x = WeaponFactory("UniqueSword")
    attack = x.make_weapon()
    print(attack)

    y = ArmorFactory("SimpleHardArmor")
    defend = y.make_armor()
    print(defend)
