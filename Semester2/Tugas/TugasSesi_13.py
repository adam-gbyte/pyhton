def konversi_interger(teks):
    try:
        teks_int = int(teks)
        print(f'Nilai integer adalah {teks_int}')
    except ValueError:
        print('Kesalahan: Integer tidak valid')


konversi_interger('123')
konversi_interger('abc')


def akses_elemen(daftar_list, index):
    try:
        hasil = daftar_list[index]
        print(f'Elemen di indeks ke {index} adalah {hasil}')
    except IndexError:
        print('Kesalahan: Indeks diluar jangkauan')


list = [1, 2, 3]
akses_elemen(list, 2)
akses_elemen(list, 5)
