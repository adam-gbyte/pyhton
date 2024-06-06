import numpy as np

names = np.array(["Reem", "Salah", "Haya", "Maryam", "Fatema"])
print(names[[2, 3, 4]])

import numpy as np

names = np.array(["Reem", "Salah", "Haya", "Maryam", "Fatema"])
names[2] = "Omar"
print(names)

import array as myarray

balance = myarray.array('i', [300, 200, 100])
print(balance[1])

import array as myarray

abc = myarray.array('q', [3, 9, 6, 5, 20, 13, 19, 22, 30, 25])
print(abc[1:4])
print(abc[7:10])

import array

balance = array.array('i', [300, 200, 100])
balance.insert(2, 150)
print(balance)

import array as myarr

a = myarr.array('b', [3, 6, 4, 8, 10, 12, 14, 16, 18, 20])
a[0] = 99
print(a)

import array as myarr

no = myarr.array('b', [10, 4, 5, 5, 7])
del no[4]
print(no)
