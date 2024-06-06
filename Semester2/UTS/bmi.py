berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (meter): "))

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
