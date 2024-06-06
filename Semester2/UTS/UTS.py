cities = "Jakarta Surabaya Bandung Malang"
city = cities.split()
word = city[3][0:]
print(word)

x = 5
y = 3.5
z = "Hello"
result = x * y / len(z)
print("result", result)

username = "admin"
password = "admin"
if username != "admin":
    if password != "admin":
        print("A")
    elif password == "admin":
        print("B")
    else:
        print("C")
else:
    if password != "admin":
        print("D")
print()
student1_grade = 89
student2_grade = 100
student3_grade = 60
if student1_grade > student2_grade:
    student1_grade = student2_grade
if student1_grade > student3_grade:
    student1_grade = student3_grade
if student2_grade > student1_grade:
    student2_grade = student1_grade
if student2_grade > student3_grade:
    student2_grade = student3_grade
if student3_grade > student1_grade:
    student3_grade = student1_grade
if student3_grade > student2_grade:
    student3_grade = student2_grade
print(student1_grade, student2_grade, student3_grade)

address = "Sukabumi"
if address == "Sukabumi":
    description = "Beautiful City"
if address != "Malang":
    description = "Not the Lion City"
elif address == "Bandung":
    description = "Flower City"
else:
    description = "Wonderful City"
print(description)

name = "Soekarno Hatta"
names = name.split()
my_name = names[len(names) - 1][-1] + names[0][0]
print(my_name)
