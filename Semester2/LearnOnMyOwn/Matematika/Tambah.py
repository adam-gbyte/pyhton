def tambah(*data) -> int | str | None:
    if len(data) == 0:
        return None

    hasil = data[0]
    proses = f'{data[0]}'

    for angka in data[1:]:
        hasil += angka
        proses += f' + {angka}'

    # print(f'{proses} = {hasil}')

    return hasil


def kurang(*data) -> int | str | None:
    if len(data) == 0:
        return None

    hasil = data[0]
    proses = f"{data[0]}"

    for angka in data[1:]:
        hasil -= angka
        proses += f" - {angka}"

    # print(f'{proses} = {hasil}')

    return hasil


def kali(*data) -> int | None | str:
    if len(data) == 0:
        return None

    hasil = data[0]
    proses = f'{data[0]}'

    for angka in data[1:]:
        hasil *= angka
        proses += f' * {angka}'

    # print(f'{proses} = {hasil}')

    return hasil


def bagi(*data) -> None | str | float:
    if len(data) == 0:
        return None

    hasil = data[0]
    proses = f"{data[0]}"

    for angka in data[1:]:
        try:
            hasil /= angka
            proses += f" / {angka}"
        except ZeroDivisionError as e:
            return 'Tidak terdefinisi'

    # print(f'{proses} = {hasil}')

    return float(round(hasil, 2))


def faktorial(n):
    if n < 0:
        return 'Tidak terdefinisi'
        # raise ValueError("Astagfirullah")
    elif n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(2, n + 1):
            hasil *= i
        return hasil


def pangkat(base, eksponen):
    return base ** eksponen


def pi():
    iterasi = 10
    pi = 3.0
    sign = 1
    for i in range(2, 2 * iterasi + 2, 2):
        pi += sign * (4 / (i * (i + 1) * (i + 2)))
        sign *= -1
    return round(pi, 2)


def luas_lingkaran(jari_jari):
    if jari_jari < 0:
        return 'Jari-jari tidak boleh negatif'

    luas = pi() * (jari_jari ** 2)
    return round(luas, 2)


print(-173 % 21)
print(-340 % 9)
print(0 % 34)
