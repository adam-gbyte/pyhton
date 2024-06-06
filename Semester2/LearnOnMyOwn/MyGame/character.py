import weapon


class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

        self.weapon = weapon.bow

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)

    def is_alive(self):
        return self.health > 0


class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.weapon = weapon.bow


class Enemy(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.weapon = weapon.gun
