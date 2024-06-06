print('segitiga for loop')

kolom = 4
baris = 1
for i in range(kolom):
    print("* " * baris)
    baris += 1

print('segitiga while loop')

kolom = 5
baris = 1
while True:
    print("* " * baris)
    baris += 1
    if baris > kolom:
        break

print('segitiga terbalik for loop')

kolom = 4
for i in range(kolom):
    print('* ' * kolom)
    kolom -= 1

print('segitiga terbalik while loop')

kolom = 4
while True:
    print("* " * kolom)
    kolom -= 1
    if kolom <= 0:
        break

print('persegi for loop')

kolom  = 4
for i in range(kolom):
    print('* ' * kolom)

print('persegi while loop')

kolom = 4
baris = 1
while True:
    print('* ' * kolom)
    baris += 1
    if baris > kolom:
        break

print('')

n = 4
for i in range(n):
    for j in range(1, n - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print('*', end=' ')
    print()
