class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage


bow = Weapon('Bow', 2)
gun = Weapon('Gun', 5)
