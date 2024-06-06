# NAMA  : ADAM GUMILANG
# NIM   : 20230040296
# KELAS : TI23C

listNama = []

while True:
    print('''\n=== MENU
    1. Menambah nama
    2. Menghapus nama
    3. Menampilkan nama
    4. Keluar aplikasi''')
    menu = input('Pilih menu : ')

    if menu == '1':
        print('\n=== MASUKKAN NAMA')
        inputNama = input('Nama: ')
        listNama.append(inputNama)

    elif menu == '2':
        print('\n=== HAPUS NAMA')
        num = 1
        for i in listNama:
            print(f'{num}. Nama : {i}')
            num += 1
        removeNama = input('Ketik nama yang ingin di hapus: ')
        listNama.remove(removeNama)
        print(f'Menghapus nama "{removeNama}" berhasil!!!')

    elif menu == '3':
        print('\n=== LIST NAMA')
        num = 1
        for i in listNama:
            print(f'{num}. Nama : {i}')
            num += 1

    elif menu == '4':
        print('\n=====')
        print('EXIT!!!')
        break

    else:
        print('Ketik 1, 2, 3, atau 4')
