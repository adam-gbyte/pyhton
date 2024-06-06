input_angka = int(input('Masukkan angka : '))

print('=== import ... as ...')

import matematika as mtk

luas_lingkaran = mtk.luas_lingkaran(radius=input_angka)
print(f'Luas lingkaran dari {input_angka} = {luas_lingkaran}')

luas_persegi = mtk.luas_persegi(sisi=input_angka)
print(f'Luas persegi dari {input_angka} = {luas_persegi}')

print('=== from ... import ... as ...')

from matematika import luas_lingkaran as luas_lngkrn, luas_persegi as luas_prsg
from matematika import *

luas_lingkaran = luas_lngkrn(radius=input_angka)
print(f'Luas lingkaran dari {input_angka} = {luas_lingkaran}')

luas_persegi = luas_prsg(sisi=input_angka)
print(f'Luas persegi dari {input_angka} = {luas_persegi}')

keliling_persegi = keliling_persegi(sisi=10)
print(f'Keliling persegi dari {input_angka} = {keliling_persegi}')
