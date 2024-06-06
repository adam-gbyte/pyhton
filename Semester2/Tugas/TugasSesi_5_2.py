print('=== Login ===')

user = input('Masukkan user name : ')
password = input('Masukkan password : ')

if user == 'admin' and password == 'admin':
    print(f'Selamat datang {user}, password anda adalah {password}')
else:
    print(f'login gagal coba lagi')


print('=== Login ===')

user = input('Masukkan user name : ')

if user == 'admin':
    password = input('Masukkan password : ')
    if password == 'admin':
        print(f'Selamat datang {user}, password anda adalah {password}')
    else:
        print(f'Login gagal, coba lagi')
else:
    print(f'Login gagal, coba lagi')

inputan = int(input('Masukkan nilai : '))

if inputan <= 59:
    print(f'Nilai anda {inputan} = E Not PASS')
elif inputan <= 69:
    print(f'Nilai anda {inputan} = D Not Satisfactory')
elif inputan <= 79:
    print(f'Nilai anda {inputan} = C Satisfying')
elif inputan <= 89:
    print(f'Nilai anda {inputan} = B Very Satisfy')
elif inputan <= 100:
    print(f'Nilai anda {inputan} = A With Compliments')
else:
    print('Masukkan nilai ulang')
