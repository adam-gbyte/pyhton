while True:
    try:
        inputan = int(input('Masukkan Umur : '))
        print(f'Umur anda : {inputan}')
        break
    except ValueError:
        print('MASUKKAN ANGKA BUKAN HURUF!!!')


x = 5
y = 0
try:
    hasil = x / y
    print(f'{x} * {y} = {hasil}')
except ZeroDivisionError:
    print('ORA BISA DIBAGI 0')


list_angka = [1, 2, 3, 4]
try:
    index = 6
    print(list_angka[index])
except IndexError:
    print(f'Tidak ada index ke {index}')


def angka_string(num1, num2, string):
    try:
        result = num1 / num2
        input_str = int(string)
        print(result)
        print(input_str)
    except ZeroDivisionError:
        print('Tidak bisa dibagi 0')
    except ValueError:
        print('Tidak bisa di convert ke INT')
angka_string(2, 0, 'abcd')
angka_string(2, 2, 'abcd')

while True:
    try:
        umur = int(input('Masukkan umur anda : '))
    except ValueError:
        print('Salah format, Masukkan angka')
    else:
        print(f'Umur anda adalah {umur}')
        break
    finally:
        print('Exception telah dilakukan')
