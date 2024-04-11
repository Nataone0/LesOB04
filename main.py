from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Sword attack")


class Bow(Weapon):
    def attack(self):
        print("Bow attack")


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        self.weapon.attack()

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon


class Monster:
    def __init__(self):
        pass


fighter = Fighter(Sword())
fighter.fight()
print("Monster down!")
fighter.change_weapon(Bow())
fighter.fight()
print("Monster down!")
