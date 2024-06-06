# print("=== NOMOR 1 ===")
#
#
# def fungsi_a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 4
#
#     return 4 * fungsi_a(n - 1) - 2
#
#
# for i in range(5):
#     n_ke_n_value = fungsi_a(i)
#     print(f"n_ke_{i} = {n_ke_n_value}")
#
# print("=== NOMOR 2 ===")
#
#
# def faktorial(n):
#     if n == 0:
#         return 3
#     elif n == 1:
#         return 6
#     elif n == 2:
#         return 0
#
#     no_1 = 2 * faktorial(n - 1) - 1
#     no_2 = faktorial(n - 1) - 2
#     no_3 = 2 * faktorial(n - 1) - 3
#
#     return no_1 + no_2 - no_3
#
#
# for i in range(10):
#     n_ke_n_value = faktorial(i)
#     print(f"n_ke_{i} = {n_ke_n_value}")


# aTuple = (100, 200, 300, 400, 500)
# print(aTuple[-2])
# print(aTuple[-4:-1])

# aTuple = (100, 200, 300, 400, 500)
# aTuple.pop(2)
# print(aTuple)

# person = {'name': 'Phill', 'age': 22}
# a = person.setdefault('age')
# print('person = ', person)
# print('Age = ', a)

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)
