# Contoh penggunaan
plain_text = "Adam Gumilang"
shift_amount = 3023
shift_amount_2 = 2


def encrypt(text, shift, shift_2):
    encrypted_text = ""
    for char in text:
        # Periksa apakah karakter merupakan huruf
        if char.isalpha():
            # Tentukan offset berdasarkan pergeseran
            offset = ord('a') if char.islower() else ord('A')
            # Enkripsi karakter
            encrypted_char = chr((ord(char) - offset + (shift + shift_2)) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            # Tambahkan karakter non-huruf tanpa enkripsi
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift, shift_2):
    decrypted_text = ""
    for char in encrypted_text:
        # Periksa apakah karakter merupakan huruf
        if char.isalpha():
            # Tentukan offset berdasarkan pergeseran
            offset = ord('a') if char.islower() else ord('A')
            # Dekripsi karakter
            decrypted_char = chr((ord(char) - offset - (shift + shift_2)) % 26 + offset)
            decrypted_text += decrypted_char
        else:
            # Tambahkan karakter non-huruf tanpa dekripsi
            decrypted_text += char
    return decrypted_text


encrypted_message = encrypt(plain_text, shift_amount, shift_amount_2)
print("Pesan terenkripsi:", encrypted_message)

shift_amount = 321
shift_amount_2 = 234

decrypted_message = decrypt(encrypted_message, shift_amount, shift_amount_2)
print("Pesan terdekripsi:", decrypted_message)
