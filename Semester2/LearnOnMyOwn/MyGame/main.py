from character import Hero, Enemy


Adam = Hero('Adam', 100)
Hawa = Enemy('Hawa', 100)


while Adam.is_alive() and Hawa.is_alive():
    input()

    Adam.attack(Hawa)
    print(f'{Adam.name} menyerang {Hawa.name} dengan {Adam.weapon.name} damage {Adam.weapon.damage}')
    if Hawa.is_alive():
        Hawa.attack(Adam)
        print(f'{Hawa.name} menyerang {Adam.name} dengan {Hawa.weapon.name} damage {Hawa.weapon.damage}')

    print(f'Health {Adam.name} = {Adam.health}')
    print(f'Health {Hawa.name} = {Hawa.health}')


if Adam.is_alive():
    print('Selamat anda menang')
elif Hawa.is_alive():
    print(f'Anda kalah')
