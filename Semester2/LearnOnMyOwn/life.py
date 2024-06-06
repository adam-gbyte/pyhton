alife = True
age = 100


def enjoy():
    print('enjoy')


def school():
    print('school')


def work():
    print('work')
    if age > 80:
        die()


def die():
    global alife
    alife = False
    print('die')


while alife:
    if age < 6:
        enjoy()
    elif 6 <= age < 18:
        school()
    elif age >= 18:
        work()
    else:
        die()
