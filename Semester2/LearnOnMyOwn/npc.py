import random


class NPC:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        damage_dealt = random.randint(0, self.damage)
        target.health -= damage_dealt
        print(f"{self.name} attack {target.name} {damage_dealt} damage.")

    def is_alive(self):
        return self.health > 0


# Fungsi untuk memeriksa kesehatan NPC
def check_npc_health(npc):
    if npc.is_alive():
        print(f"{npc.name} = {npc.health}")
    else:
        print(f"{npc.name} telah mati.")


# Membuat beberapa NPC
player = NPC("Ambatron", 100, 20)
enemy = NPC("Megatron", 100, 30)

# Permainan dimulai
print("Game dimulai!")
while player.is_alive() and enemy.is_alive():
    input()
    # Pemain menyerang musuh
    player.attack(enemy)
    check_npc_health(enemy)
    # Musuh menyerang pemain
    if enemy.is_alive():
        enemy.attack(player)
        check_npc_health(player)

# Menampilkan hasil akhir permainan
if player.is_alive():
    print("Selamat, Anda menang!")
else:
    print("Anda kalah, coba lagi.")
