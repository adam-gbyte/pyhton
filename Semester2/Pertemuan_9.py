cars = ['toyota', 'daihatsu', 'honda']

for i in cars:
    print(i)

cars = ['toyota', 'daihatsu', 'honda']

x = cars[0]
print(x)

cars = ['toyota', 'daihatsu', 'honda']

cars[0] = 'nissan'
print(cars)

cars = ['toyota', 'daihatsu', 'honda']

cars.append('nissan')
print(cars)
cars.remove('toyota')
print(cars)
cars.pop(1)
print(cars)

import numpy as np

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

arr1 = np.array(list1)
arr2 = np.array(list2)

arr3 = arr1 * arr2
print(arr3)
