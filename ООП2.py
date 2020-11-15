class Weapon:
    def __init__(self, damage):
        self.damage = damage


class Bow(Weapon):
    def __init__(self):
        super().__init__(25)


class Sword(Weapon):
    def __init__(self):
        super().__init__(40)


class Staff(Weapon):
    def __init__(self):
        super().__init__(30)


class Inventory:
    def __init__(self, sword, holy_dust):
        self.sword = sword
        self.holy_dust = holy_dust


class Mob:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health


class Beast(Mob):
    def __init__(self, damage, health):
        super().__init__(damage, health)


class Demon(Mob):
    def __init__(self, damage, health):
        super().__init__(damage, health)


class Elemental(Mob):
    def __init__(self, damage, health):
        super().__init__(damage, health)


class Orc(Mob):
    def __init__(self, damage, health):
        super().__init__(damage, health)



class Trader:
    def __init__(self, holy_dust_price):
        self.holy_dust_price = holy_dust_price


class GoodNPC:
    def __init__(self, task):
        self.task = 'В лесу близ города Акрополь завелись страшные демоны-сатанисты, вооруженные посохами. Избавься от них!'

    def task_s(self):
        print(task)


class EvilNPC:
    pass


class Habitat:
    pass


class MainCharacter:
    def __init__(self, money, health):
        self.money = money
        self.health = health

    def attack_beast(self):
        self.health -= Beast.damage

    def attack_demon(self):
        self.health -= Demon.damage

    def attack_elemental(self):
        self.health -= Elemental.damage

    def attack_orc(self):
        self.health -= Orc.damage

    def hit_orc(self):
        Orc.health -= Sword.damage

    def hit_beast(self):
        Beast.health -= Sword.damage

    def hit_demon(self):
        Demon.health -= Sword.damage

    def hit_elemental(self):
        Elemental.health -= Sword.damage