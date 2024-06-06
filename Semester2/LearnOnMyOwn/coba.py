def hello(text, panjang):
    sisa = panjang % len(text) - 1
    teks = text[sisa]
    print(f'Teks ke {panjang} adalah', teks)


hello('POLSEK', 457394)

print(7 % (5 // 2))
print((3 ** 2) // 2)
print(100 // 42)
print(10 ** 5)

print((5 > 10 and 'a > b') or (10 > 5 and 'b > a'))

print("======================")
products = ["apples", "oranges", "bananas"]
products[2] =  "lime"
print(products[2])
