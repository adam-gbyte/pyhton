while True:
    print("""
=============
MENU:
1. Menghitung usia saat ini
2. Menghitung sisa tahun angsuran
3. Menentukan berat badan (BMI)
4. Quit""")

    pilihan = input('Masukkan pilihan anda (1/2/3/4) : ')

    if pilihan == '1':
        tahun_kelahiran = int(input("Masukkan tahun kelahiran : "))
        tahun_saat_ini = int(input("Masukkan tahun saat ini : "))

        usia_saat_ini = tahun_saat_ini - tahun_kelahiran

        print(f"Umur anda saat ini : {usia_saat_ini}")

    elif pilihan == '2':
        jumlah_angsuran = int(input("Masukkan jumlah angsuran: "))
        sudah_dibayar = int(input("Masukkan jumlah angsuran yang sudah dibayar: "))

        sisa_angsuran = jumlah_angsuran - sudah_dibayar
        sisa_tahun = sisa_angsuran / 12

        print("sisa angsuran:", sisa_angsuran)
        print("Sisa tahun angsuran:", sisa_tahun)

    elif pilihan == '3':
        berat_badan = float(input("Masukkan berat badan Anda (KILOGRAM): "))
        tinggi_badan = float(input("Masukkan tinggi badan Anda (METER): "))

        bmi = berat_badan / (tinggi_badan ** 2)

        if bmi < 18.5:
            kategori = "Kurus"
        elif bmi >= 18.5 and bmi < 25:
            kategori = "Normal"
        elif bmi >= 25 and bmi < 30:
            kategori = "Kegemukan"
        else:
            kategori = "Obesitas"

        print("BMI Anda adalah:", bmi)
        print("Kategori BMI Anda:", kategori)

    elif pilihan == '4':
        print("Keluar dari aplikasi, Terima kasih!")
        break

    else:
        print("PILIHAN ANDA TIDAK VALID. PILIH 1, 2, 3, ATAU 4.")
