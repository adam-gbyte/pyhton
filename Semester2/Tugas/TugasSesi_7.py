while True:
    print("""
=============
MENU:
1. Menghitung luas segitiga
2. Menghitung luas persegi panjang
3. Menentukan angka ganjil dan genap
4. Quit""")
    pilihan = input('Masukkan pilihan anda (1/2/3/4) : ')

    if pilihan == '1':
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))

        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah:", luas)

    elif pilihan == '2':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))

        luas = panjang * lebar
        print("Luas persegi panjang adalah:", luas)

    elif pilihan == '3':
        angka = int(input("Masukkan angka: "))

        if angka % 2 == 0:
            hasil = "GENAP"
        else:
            hasil = "GANJIL"

        print(f"Angka {angka} tersebut adalah angka", hasil)

    elif pilihan == '4':
        print("Keluar dari aplikasi, Terima kasih!")
        break

    else:
        print("PILIHAN ANDA TIDAK VALID. PILIH 1, 2, 3, ATAU 4.")
