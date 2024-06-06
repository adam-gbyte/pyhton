# Variabel dan Tipe Data

panjang = 5 # Integer
lebar = 10.5 # Float
luas = panjang * lebar

print("{} * {} = {}".format(panjang, lebar, luas))
print("Tipe data dari panjang =", type(panjang))
print("Tipe data dari lebar =", type(lebar))
print("Tipe data dari luas =", type(luas))

print("\n======= Tipe Data String ======\n")

nama_depan = "Adam"
nama_belakang = "Gumilang"
nama_lengkap = nama_depan + ' ' + nama_belakang
usia = '18'
alamat = 'Cibadak'
kata_mutiara = 'Jangan pernah menyerah'

print(nama_lengkap, '(' + usia + ')', ',', 'dari', alamat, ',', 'kata mutiara:', kata_mutiara)

print('\nTipe data dari nama_lengkap', type(nama_lengkap))
print('Tipe data dari usia', type(usia))
print('Tipe data dari alamat', type(alamat))
print('Tipe data dari kata mutiara', type(kata_mutiara))
