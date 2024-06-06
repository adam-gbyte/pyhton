jumlah_angsuran = int(input("Masukkan jumlah angsuran: "))
sudah_dibayar = int(input("Masukkan jumlah angsuran yang sudah dibayar: "))

sisa_angsuran = jumlah_angsuran - sudah_dibayar
sisa_tahun = sisa_angsuran / 12

print("sisa angsuran:", sisa_angsuran)
print("Sisa tahun angsuran:", sisa_tahun)
