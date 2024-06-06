# from luas.segitiga import luas_segitiga
# from luas import lingkaran, persegi
# from volume.kubik import volume_kubik
# import volume.bola
# from volume.trapesium import *

"""
NAMA : ADAM GUMILANG
NIM : 20230040296
"""

from luas import lingkaran, persegi, segitiga
from volume import bola, kubik, trapesium

while True:
    print('''=== MENU
    1. Luas Lingkaran
    2. Luas Persegi
    3. Luas Segitiga
    4. Volume Bola
    5. Volume Kubik
    6. Volume Trapesium
    7. Exit''')

    input_menu = int(input('MENU, (1, 2, 3, 4, 5, 6, atau 7): '))

    if input_menu == 1:
        print('=== Luas Lingkaran')
        angka1 = int(input('Masukkan radius : '))
        hasil = lingkaran.luas_lingkaran(angka1)
        print(f'Luas Lingkaran = {hasil}')

    elif input_menu == 2:
        print('=== Luas Persegi')
        angka1 = int(input('Masukkan sisi : '))
        hasil = persegi.luas_persegi(angka1)
        print(f'Luas Persegi = {hasil}')

    elif input_menu == 3:
        print('=== Luas Segitiga')
        angka1 = int(input('Masukkan alas : '))
        angka2 = int(input('Masukkan tinggi : '))
        hasil = segitiga.luas_segitiga(angka1, angka2)
        print(f'Luas Segitiga = {hasil}')

    elif input_menu == 4:
        print('=== Volume Bola')
        angka1 = int(input('Masukkan radius : '))
        hasil = bola.volume_bola(angka1)
        print(f'Volume Bola = {hasil}')

    elif input_menu == 5:
        print('=== Volume Kubik')
        angka1 = int(input('Masukkan sisi : '))
        hasil = kubik.volume_kubik(angka1)
        print(f'Volume Kubik = {hasil}')

    elif input_menu == 6:
        print('=== Volume Trapesium')
        angka1 = int(input('Masukkan alas atas : '))
        angka2 = int(input('Masukkan alas bawah : '))
        angka3 = int(input('Masukkan tinggi : '))
        hasil = trapesium.volume_trapesium(angka1, angka2, angka3)
        print(f'Volume Trapesium = {hasil}')

    elif input_menu == 7:
        print('Exit')
        break

    else:
        print('Pilih 1, 2, 3, 4, 5, 6, atau 7')
